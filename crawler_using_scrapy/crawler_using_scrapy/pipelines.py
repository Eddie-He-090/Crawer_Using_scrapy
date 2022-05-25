# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


class CrawlerUsingScrapyPipeline:
    def process_item(self, item, spider):
        first_ReportIDIssueTime = "2022-02-28"
        addresses = [
            "2021022249@m.scnu.edu.cn",
        ]
        try:
            print("\nitem:", item["first_ReportIDIssueTime"], "\n")
            if item["first_ReportIDIssueTime"] == first_ReportIDIssueTime:
                print("\nNo update!\n")
            else:
                print("\nContent updated!\n")
                self.send(destinations=addresses)
        except:
            print("\nError occurs when applying process_item in pipeline.py!\n")
        return item

    def send(self, destinations):
        mail_host = "smtp.126.com"
        mail_user = "cy0240"
        mail_pass = "VLSHXPAOYNGSQTBK"
        sender = "cy0240@126.com"
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
            smtpObj.connect(mail_host, 25)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, destinations, message.as_string())
            print(
                "\nThe e-mails have been sent to {} receivers.\n".format(
                    len(destinations)
                )
            )
            for destination in destinations:
                print("\nThe e-mails have been sent to {} .\n".format(destination))
            smtpObj.quit()
        except smtplib.SMTPException:
            print("\nError: can not send e-mails.\n")
