import smtplib
from email.message import EmailMessage

def send_alert(log_line):
    msg = EmailMessage()
    msg.set_content(f"🚨 Critical Error Detected:\n\n{log_line}")

    msg['Subject'] = "⚠️ Log Monitor Alert: CRITICAL ERROR"
    msg['From'] = "lavanyamargam61@gmail.com"
    msg['To'] = "21.624lavanyamargam@gmail.com"

    # Gmail SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("lavanyamargam61@gmail.com", "qnob ybor gqhs uulr")
        smtp.send_message(msg)
