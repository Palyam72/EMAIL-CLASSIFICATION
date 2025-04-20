import requests

url = "https://Rohith25Jan-email-classification.hf.space/classify_email"
headers = {"Content-Type": "application/json"}

test_email = {
    "email_body": "Hello, my name is John Doe. My email is johndoe@example.com. I need help with my billing issue for card 4111-1111-1111-1111."
}

response = requests.post(url, json=test_email, headers=headers)

# print("Status code:", response.status_code)

try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Failed to parse response as JSON.")
    print("Raw response:", response.text)
