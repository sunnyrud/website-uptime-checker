import requests
import smtplib
from email.mime.text import MIMEText
import time

URL = "https://awerre.com"
EMAIL_ADDRESS = "vpnindonesia154@gmail.com"
EMAIL_PASSWORD = "ujiv dyrv rjzs crte"
TO_EMAIL = "saitejasunny99999@gmail.com"

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False

def send_notification():
    msg = MIMEText("Your website is down!")
    msg['Subject'] = 'Website Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

while True:
    if not check_website(URL):
        send_notification()
        print("Website down! Notification sent.")
    else:
        print("Website up.")
    time.sleep(60)  # check every minute
