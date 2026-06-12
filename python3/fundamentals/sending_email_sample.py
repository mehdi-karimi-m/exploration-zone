from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

message = MIMEMultipart()
message["from"] = "Mehdi Karimi"
message["to"] = "mina.taheri@gmail.com"
message["subject"] = "I Love You"
#message.attach(MIMEText("Some test as a body", "plain"))
template = Template(Path("template.html").read_text())
template.substitute({
    "name": "Mina Jon"
})
message.attach(MIMEText(template, "html"))
message.attach(MIMEImage(Path("hart.jpg").read_bytes()))

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.helo()
    smtp.starttls()
    smtp.login("test@gmail.com", "testpassword")
    smtp.send_message(message)
    print("Email sent...")
