import os
from getpass import getpass
from time import sleep

import pandas as pd
import typer
from certifigen.email import EmailSender
from certifigen.generator import generate_certificate

COLUMNS_EXPECT = ["name", "mail", "work", "plenary_speaker"]


def main(path_csv: str):
    # Read the table containing the participants
    df = pd.read_csv(path_csv)

    # Check that the columns are as expected
    list_missing = list(set(COLUMNS_EXPECT) - set(df.columns))
    if len(list_missing) > 0:
        raise ValueError(f"The following columns are missing: {list_missing}")

    # Create the "certificates" folder
    if not os.path.exists("certificates"):
        os.mkdir("certificates")

    # Ask for email and passwordd
    sender = input("Email sender: ")
    password = getpass("Password: ")

    # Login
    try:
        email = EmailSender(sender, password)
    except:
        print("Could not connect to email. Generating certificates anyway.")

    # Generate the certificates for each participant
    for idx, row in df.iterrows():
        # Relevant participant information
        name = row["name"].upper()
        mail = row["mail"]
        try:
            user = mail.split("@")[0]
        except AttributeError:
            print(f"[ERROR] No email for {name}")
            user = name.replace(" ", "-")
        # Get the work title
        work = row["work"]
        # Certificate of poster presentation or talk
        if len(work) > 0:
            is_plenary_speaker = row["plenary_speaker"]
        # Certificate of assistance
        else:
            work = None
            is_plenary_speaker = False
        generate_certificate(
            name, user, work=work, is_plenary_speaker=is_plenary_speaker
        )
        # Send the email with the attached pdf
        email.send_email_pdf(f"certificates/{user}.pdf", mail)
        # Wait a second between each email
        sleep(1)


if __name__=="__main__":
    typer.run(main)