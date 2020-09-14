import sendgrid
import os
from sendgrid.helpers.mail import *
from dotenv import load_dotenv
load_dotenv()

# input sender email address and password:
from_addr =input("from")
to_addr =input("to:")
# input receiver email address.

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("sendgrid_key"))
from_email = Email(to_addr)
to_email = To(to_addr)
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)