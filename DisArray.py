import imapclient,pyzmail,webbrowser,subprocess,pyautogui,threading,time,os,datetime
import yagmail as email
import pywhatkit as kit

def get_email():
    
    dict={'Brave':"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",'VSCode':"C:\\Users\\Sujay S C\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"}
    server=imapclient.IMAPClient('imap.gmail.com',ssl=True)
    server.login('cleversquadtech@gmail.com','pwejkovsibyxaqfe')
    server.select_folder('INBOX',readonly=False)
    UIDs=server.search(['FROM' ,'abhi12ravi@gmail.com'])
    print(UIDs)
    instructions=[]
    for uid in UIDs:
        rawMessage=server.fetch(uid,['BODY[]','FLAGS'])
        message=pyzmail.PyzMessage.factory(rawMessage[uid] [b'BODY[]'])