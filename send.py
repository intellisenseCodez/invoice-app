from email.message import EmailMessage
import smtplib

import store

def send_email(sender_email,sender_password,receiver_email,subject, body):

    em = EmailMessage()

    em["From"] = sender_email
    em["To"] = receiver_email
    em['Subject'] = subject
    em.set_content(body)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, receiver_email, em.as_string())