import imaplib
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import webbrowser
import subprocess
import pyautogui
import threading
import time
import os
import datetime
import yagmail
import pywhatkit as kit

def get_email():
    dict = {'Brave': "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
            'VSCode': "C:\\Users\\Sujay S C\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"}

    server = imaplib.IMAP4_SSL('imap.gmail.com')
    server.login('cleversquadtech@gmail.com', 'pwejkovsibyxaqfe')
    server.select('inbox')
    status, messages = server.search(None, '(FROM "abhi12ravi@gmail.com")')
    instructions = []

    for msg_id in messages[0].split():
        _, msg_data = server.fetch(msg_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    instructions.append(part.get_payload(decode=True).decode(part.get_content_charset()))

    server.close()

    for instruction in instructions:
        print(instruction.split())
        for instruct in instruction.split():
            print(instruct)
            if 'torrent' in str(instruct) or str(instruct).startswith("magnet:?"):
                torrent = subprocess.Popen(["C:\Program Files\qBittorrent\qbittorrent.exe", str(instruct)])

                if torrent.poll() is None:
                    print('Process is still running')
                    time.sleep(10)
                    pyautogui.press('enter')
                    send_confirmation('qBittorrent', f"qBittorrent is up and running.")

            for app in dict.keys():
                if "Openall:" in instruct:
                    application = subprocess.Popen(dict[app])
                    if application.poll() is None:
                        print("Process running successfully")
                        send_confirmation(app, f"{app} is up and running: {app} is online!!!")

                if "Open:" in instruct:
                    application = subprocess.Popen(dict[app])
                    if application.poll() is None:
                        print("Process running successfully")
                        send_confirmation(app, f"{app} is up and running: {app} is online!!!!")

                if 'SOS' in instruct:
                    sos()

def send_confirmation(process, body, attachment=None):
    sender_email = 'cleversquadtech@gmail.com'
    receiver_email = 'boodelyboo1234@gmail.com'

    yag = yagmail.SMTP(sender_email, 'pwejkovsibyxaqfe')

    if attachment:
        yag.send(receiver_email, f"{process} is running.", [body, attachment])
    else:
        yag.send(receiver_email, f"{process} is running.", body)

    yag.close()

def sos():
    import requests
    import json

    send_url = "http://api.ipstack.com/check?access_key=9218a6e821aca6b2d9e0b6111b782759"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    print(geo_json)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    print(latitude)
    print(longitude)
    webbrowser.open(f'https://maps.google.com/?q={latitude},{longitude}')
    current_time = datetime.datetime.now()
    kit.sendwhatmsg_instantly(phone_no='+91 6362678349',
                              message=f'This is an SOS from Suhas, this is his latest location https://maps.google.com/?q={latitude},{longitude} ')

get_email()
