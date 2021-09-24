import requests # http requests
import bs4 # web scraping
import smtplib # send email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime #system date and time manipulation

now = datetime.datetime.now()
# print(now)

# email content placeholder
content = ''

def extract_news(url):
    print("Extracting Hacker News Stories...")
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign':''})):
        cnt += ((str(i+1) + ' :: ' + tag.text + "\n" + "<br>") if tag.text != 'More' else '')
    return (cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>----------<br>')
content += ('<br><br>End of Message')

# print(content)

