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
    print("Extracting Unix Community Queries...")
    cnt = ''
    cnt += (f'<b>Unix Community Queries for {now.day}-{now.month}-{now.year}:</b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('span', attrs={'class':'link-top-line'})):
        cnt += ((str(i+1) + f' :: <a href="{tag.find("a", href=True)["href"]}">{tag.text}</a>' + "<br>") if tag.text != 'More' else '')
    return (cnt)

with open("output.html", "w", encoding = 'utf-8') as file:
    cnt = extract_news('https://community.unix.com/')
    content += cnt
    content += ('<br>----------<br>')
    content += ('<br><br>End of Message')
    file.write(content)


