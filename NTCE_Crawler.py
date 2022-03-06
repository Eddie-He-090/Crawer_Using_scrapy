import json
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import msvcrt


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
            for destination in destinations:
                print("The e-mails have been sent to {} .".format(destination))
            smtpObj.quit()
        except smtplib.SMTPException:
            print("Error: can not send e-mails.")


class Spider:
    def fetch(self):
        url = "https://ntce.neea.edu.cn"
        try:
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            ksdt = soup.find(string="考试动态").parent.get("href")
            print("url + ksdt: ", url + ksdt)
            try:
                r2 = requests.get(url + ksdt)
                r2.encoding = r2.apparent_encoding
                r2.raise_for_status()
                soup2 = BeautifulSoup(r2.text, "html.parser")
                listdiv = soup2.find("div", class_="listdiv")
                first_data = listdiv.find("ul", id="first_data")
                li = first_data.find_all("li")
                first_ReportIDIssueTime = (
                    li[0].find("span", id="ReportIDIssueTime").string
                )
                print("first_ReportIDIssueTime from NTCE: ", first_ReportIDIssueTime)
                return first_ReportIDIssueTime
            except:
                print(
                    "Error occurs when applying request.get(ksdt)! \nr2.status_code: ",
                    r.status_code,
                )
        except:
            print(
                "Error occurs when applying request.get(https://ntce.neea.edu.cn)! \nr.status_code: ",
                r.status_code,
            )

    def verify(self, first_ReportIDIssueTime):
        with open("./ReportIDIssueTime.json", "r") as f:
            ReportIDIssueTime = json.load(f)
            print(
                "first_ReportIDIssueTime from json: ",
                ReportIDIssueTime["first_ReportIDIssueTime"],
            )
            f.close()
        if first_ReportIDIssueTime == ReportIDIssueTime["first_ReportIDIssueTime"]:
            print("No update!")
            return True
        else:
            with open("./ReportIDIssueTime.json", "w") as f2:
                ReportIDIssueTime["first_ReportIDIssueTime"] = first_ReportIDIssueTime
                json.dump(ReportIDIssueTime, f2)
                f2.close()
            print("Content updated!")
            return False


if __name__ == "__main__":
    Spider = Spider()
    first_ReportIDIssueTime = Spider.fetch()
    if Spider.verify(first_ReportIDIssueTime) is not True:
        with open("./receivers.json", "r") as file:
            receivers = json.load(file)
            file.close()
        Postman = Postman()
        Postman.send(receivers["addresses"])
