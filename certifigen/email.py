import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unittest.util import strclass


class EmailSender:
    def __init__(self, sender: str, password: str):
        self.sender = sender
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.ehlo()
        self.server.login(sender, password)

    def send_email_pdf(self, path_pdf: strclass, destination: str, name: str):
        # Craft message (obj)
        msg = MIMEMultipart()

        msg["Subject"] = "Marcellán Fest - Certificate of assistance"
        msg["From"] = self.sender
        msg["To"] = destination
        # Insert the text to the msg going by e-mail
        msg.attach(
            MIMEText(
                "Dear participant,\n"
                "You will find your certificates of assistance to the International Conference on Orthogonal Polynomials attached below.\n"
                "Best regards,\n \n David Gómez-Ullate",
                "plain",
            )
        )
        # Attach the pdf to the msg going by e-mail
        with open(path_pdf, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header(
                "Content-Disposition", "attachment", filename=path_pdf.split("/")[-1]
            )
            msg.attach(attach)
        # send msg
        try:
            self.server.send_message(msg)
        except IndexError:
            print(f"[ERROR] Could not sent email to {name}")
