import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


class Postman:
    def __init__(self):
        self.mail_host = "smtp.126.com"
        self.mail_user = "cy0240"
        self.mail_pass = "VLSHXPAOYNGSQTBK"
        self.sender = "cy0240@126.com"
        # self.receivers = "cy0240@126.com,13612717888@139.com"

    def send(self, destinations):
        message = MIMEMultipart()
        text = MIMEText(
            "The content of NTCE websites has been updated. Please check it out!"
            + "\nThe link is https://ntce.neea.edu.cn/ ."
            + "\n"
            + "\nIf any question about this crawler occurs, you could just reply to this e-mail. I will git in touch with you in a week, hopefully.",
            "plain",
            "utf-8",
        )
        message.attach(text)
        message["From"] = "Eddie He<20210222490@m.scnu.edu.cn>"
        message["Subject"] = Header("Update Notification of NTCE Website", "utf-8")
        message["To"] = "You"
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, destinations, message.as_string())
            print(
                "The e-mails have been sent to {} receivers.".format(len(destinations))
            )
            smtpObj.quit()
        except smtplib.SMTPException:
            print("Error: can not send e-mails.")


if __name__ == "__main__":
    with open("./receivers.json", "r") as file:
        receivers = json.load(file)
        file.close()

    Postman = Postman()
    Postman.send(receivers["addresses"])
