import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, receiver, subject, message):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        server.quit()

if __name__ == "__main__":
    send_email(
        sender=input("Sender email: "),
        password=input("App password: "),
        receiver=input("Receiver email: "),
        subject="Test Email",
        message="Hello from your Python automation script!"
    )
