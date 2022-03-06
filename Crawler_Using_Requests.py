import json
import requests
from bs4 import BeautifulSoup


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

        with open("./ReportIDIssueTime.json", "r") as f:
            ReportIDIssueTime = json.load(f)
            print(
                "first_ReportIDIssueTime from json: ",
                ReportIDIssueTime["first_ReportIDIssueTime"],
            )
            if first_ReportIDIssueTime == ReportIDIssueTime["first_ReportIDIssueTime"]:
                pass
            else:
                with open("./ReportIDIssueTime.json", "w") as f2:
                    ReportIDIssueTime[
                        "first_ReportIDIssueTime"
                    ] = first_ReportIDIssueTime
                    json.dump(ReportIDIssueTime, f2)
                    f2.close()
            f.close()


if __name__ == "__main__":
    Spider = Spider()
    Spider.fetch()
