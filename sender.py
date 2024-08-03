import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def email_alert(to, subject, body):
    user = os.getenv("SENDER_USER")
    password = os.getenv("SENDER_PASSWORD")
    

    # Create the message
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    # Connect to SMTP server and send the email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

    print("Email successfully sent.")

if __name__ == "__main__":
    to = input("Enter the email address : ")
    subject = input("Enter the subject : ")
    body = input("Enter the body of your email : ")
    email_alert(to, subject, body)