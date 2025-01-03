import smtplib
from email.message import EmailMessage


Password = "password here"
sender = "sender email"
receiver = "receiver email"


def send_email(name,lastname,email,date,occupation):
    email_message= EmailMessage()
    email_message["Subject"] = "New employee"
    email_message.set_content(f"Name :{name} {lastname}\nEmail :{email}\nDate :{date}\nOccupation :{occupation}")



    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender,Password)
    gmail.sendmail(sender,receiver,email_message.as_string())
    gmail.quit()