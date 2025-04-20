from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from api import classify_email

app = FastAPI(
    title="Email Classification API",
    description="API that masks PII and classifies emails into predefined categories",
    version="1.0"
)

# Define the expected JSON schema
class EmailRequest(BaseModel):
    email: str

@app.post("/classify_email")
async def classify(request: EmailRequest):
    """
    Accepts JSON input with an 'email' field, masks PII, and classifies the email.
    """
    try:
        if not request.email:
            raise HTTPException(status_code=400, detail="Email field is required.")

        # Process the email
        return classify_email(request.email)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
