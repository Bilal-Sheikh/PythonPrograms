import smtplib 
from email.message import EmailMessage
from unicodedata import name

def emailAlert(to, subject, body):
    message = EmailMessage()
    message.set_content(body)
    message['to'] = to
    message['subject'] = subject

    username = "coeta.attendance.alerts@gmail.com"
    message['from'] = username
    password = "smasyohyxcovuixf"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username, password)
    server.send_message(message)
    server.quit()

if __name__ == '__main__':

    emailAlert("72bilal.sheikh@gmail.com", "Attendance Alert",
    "Your ward was absent")