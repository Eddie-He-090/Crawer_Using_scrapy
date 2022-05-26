# Introduction

## Function

Periodically run the `crawler.py` to check weather there is update in the ntce website.

If the "考试动态" is updated, a notification e-mail will be sent to your mail box.

## Usage

### Run it by yourself

1. Install Python 3 + .

2. Install requests，BeautifulSoup4.

3. Download the code files. **Make sure the `crawler.py`, `receivers.json`, `ReportIDIssueTime.json` are in the same folder.**.

4. Add a periodical tast to run the `crawler.py`.

5. Add your e-mail address in the `receivers.json` and it will work, hopefully.

### Let me run it for you

There are 2 ways to do it:

1. Add your e-mail address in the `receivers.json` and open a Pull Request.

2. Contact me to inform your e-mail address.

## Warnning

The program should work well theoretically. But don't rely on it 100 %. You should also check the exam news manually.

If you miss a exam or a piece of news, you could blame the program as well as me, but I would not take the responsibility for it.

## Asking for help

* I have tried to use pyinstaller to pack a `.exe` file. Unfortunately it doesn't work.

* I have also tried to use scrapy. The program work well in my PC and on the zyte.com . Unfortunately, it costs quite a lot to add a periodical task on the zyte.com.

If there are free ways to deploy this crawler, I will appreciate it if you could tell me. (This crawler only generate tiny flow and to be honest, I sincerely don't want to pay for it as it's not necessary.)

## Fun

That's me who missed the exam in March, 2022[^1]!

[^1]:You could find my complaint here:
[大头虾竟然没报名教资考试！！！](https://www.douban.com/note/826618560/)
