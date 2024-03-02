import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

# ENTER EMAIL CREDENTIALS
SENDER_EMAIL = "nishant.mishra550@gmail.com"
SENDER_PASSWORD = getpass.getpass("Enter your password: ")

# DO NOT TOUCH
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_email(recipient, subject, body, attachment_path):
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = recipient
    message["Subject"] = subject

    # Attaches text part of th mail to the message
    message.attach(MIMEText(body, "plain"))

    # Attaches the attachment to the mail
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            # CHANGE THE NAME OF THE FILE TO BE ATTACHED
            part.add_header(
                "Content-Disposition",
                "attachment; filename= My Attachment.pdf",
            )
            message.attach(part)

    # this is the part that sends the mails out. this is also shit code dont worry about it :)
    print(f"Sending mail to {recipient}", end="\t")
    server.send_message(message)
    print("✅  Sent!")


def main():
    # CHANGE MAIL CONTENT HERE
    email_subject = "<Sample Subject>"
    email_body = """
    Enter email contents here

    Multiline is supported
    """

    # COMMENT THE LINE BELOW IF YOU DO NOT WANT TO ATTACH ANY FILE
    # ALSO UNCOMMENT THE LINE THAT SAYS attachment_path = None
    attachment_path = "./attachments/sample.pdf"
    # attachment_path = None

    # Recipients will be read from a file. Do not touch any of this
    recipients = list()
    with open("recipients.txt") as f:
        recipients = [x.strip() for x in f.readlines()]

    for recipient in recipients:
        send_email(recipient, email_subject, email_body, attachment_path)


if __name__ == "__main__":
    server = SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    main()
    server.quit()
