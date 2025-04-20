from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from groq import Groq
import json
import re

from api import classify_email

sample_data = """
Change : Subject: Request to add new field in customer onboarding form

Hello,

We need to add a “Preferred Communication Channel” field to the customer onboarding form in the CRM. Please plan this change and let us know the timeline.

Thanks,  
Shalini Gupta

Incident : Subject: Email delivery delay

Hi Support,

Emails are taking more than 30 minutes to deliver, both internal and external. This started happening since this morning.

Please resolve this as soon as possible.

Regards,  
Tarun Bhatia

Request : Subject: Request for access to JIRA project

Hi Team,

Please grant me access to the “Alpha Release” project in JIRA. I need it for tracking and updating tasks assigned to me.

Best,  
Ayesha Rizvi

Problem : Subject: Recurring authentication failures for multiple users

Hi,

Several users in the finance department are repeatedly getting authentication errors when logging into the internal portal. This has been happening for the last 2 weeks.

Please look into this and resolve the root cause.

Thanks,  
Vikram Chauhan
"""

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/classify", response_class=HTMLResponse)
async def classify(
    request: Request,
    email: str = Form(...),
    mode: str = Form("ml"),
    api_key: str = Form(None)
):
    if mode == "llm":
        try:
            if not api_key:
                raise ValueError("API Key is required for LLM mode")

            groq_client = Groq(api_key=api_key)

            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an email classification system. Mask PII and classify the email "
                        "into predefined support categories: Change, Incident, Problem, and Request.\n"
                        "Return output strictly as a JSON object with these keys:\n"
                        "- masked_email: string\n"
                        "- entities: list of objects with 'entity' and 'classification'\n"
                        "- category: one of Change, Incident, Problem, Request\n"
                        "No markdown or explanation.\n"
                        f"Sample data : {sample_data}"
                    )
                },
                {
                    "role": "user",
                    "content": f"Classify and mask the following email:\n\n{email}"
                }
            ]

            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )

            raw_text = response.choices[0].message.content.strip()

            # Safely extract JSON object
            match = re.search(r"\{.*\}", raw_text, re.DOTALL)
            if not match:
                raise ValueError("Could not extract JSON from LLM response")

            parsed = json.loads(match.group())

            return templates.TemplateResponse("index.html", {
                "request": request,
                "input_email": email,
                "masked_email": parsed.get("masked_email", "N/A"),
                "entities": parsed.get("entities", []),
                "category": parsed.get("category", "N/A")
            })

        except Exception as e:
            return templates.TemplateResponse("index.html", {
                "request": request,
                "input_email": email,
                "masked_email": "Error",
                "entities": [],
                "category": f"LLM Error: {str(e)}"
            })

    else:
        result = classify_email(email)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "input_email": result["input_email_body"],
            "masked_email": result["masked_email"],
            "entities": result["list_of_masked_entities"],
            "category": result["category_of_the_email"]
        })
