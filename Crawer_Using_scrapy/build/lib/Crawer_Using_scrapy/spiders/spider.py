from bs4 import BeautifulSoup
import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    # allowed_domains = ["https://ntce.neea.edu.cn"]
    start_urls = ["https://ntce.neea.edu.cn"]

    def parse(self, response):
        try:
            url = "https://ntce.neea.edu.cn"
            # yield scrapy.Request(url)
            ntce = response.body.decode("utf-8")
            # print(ntce)
            with open("ntce.html", "wb") as f:
                f.write(response.body)
                f.close()
            soup = BeautifulSoup(ntce, "html.parser")
            # print(type(soup))
            ksdt = soup.find(string="考试动态").parent.get("href")
            print("\nurl + ksdt:", url + ksdt, "\n")
            try:
                yield scrapy.Request(
                    url + ksdt, callback=self.extract_first_ReportIDIssueTime
                )
            except:
                print("\nError occurs when applying request.get(ksdt)!\n")
        except:
            print("\nError occurs when applying request.get(ntce)!\n")

    def extract_first_ReportIDIssueTime(self, response):
        infoDict = {}
        ksdt = response.body.decode("utf-8")
        # print(ksdt)
        with open("ksdt.html", "wb") as f2:
            f2.write(response.body)
            f2.close()
        soup2 = BeautifulSoup(ksdt, "html.parser")
        listdiv = soup2.find("div", class_="listdiv")
        first_data = listdiv.find("ul", id="first_data")
        li = first_data.find_all("li")
        first_ReportIDIssueTime = li[0].find("span", id="ReportIDIssueTime").string
        print("\nfirst_ReportIDIssueTime:", first_ReportIDIssueTime, "\n")
        infoDict["first_ReportIDIssueTime"] = first_ReportIDIssueTime
        yield infoDict
