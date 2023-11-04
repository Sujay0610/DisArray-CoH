from flask import Flask, request, jsonify
import imapclient,pyzmail,webbrowser,subprocess,pyautogui,threading,time,os,datetime
import yagmail as email
import pywhatkit as kit

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_instructions():
    data = request.get_json()
    instructions = data.get('instructions', [])

    response_messages = []
    for instruction in instructions:
        response = execute_instruction(instruction)
        response_messages.append(response)

    return jsonify({'responses': response_messages})

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
        
    

        if message.text_part != None:
            print(message.text_part.get_payload().decode(message.text_part.charset))
            instructions.append(message.text_part.get_payload().decode(message.text_part.charset))
            
        # server.delete_messages(uid)
    server.logout()
   

    for instruction in instructions:
        print(instruction.split())
        for instruct in instruction.split():
            print(instruct)
            if 'torrent' in str(instruct) or str(instruct).startswith("magnet:?"):
                torrent=subprocess.Popen(["C:\Program Files\qBittorrent\qbittorrent.exe",str(instruct)])

                if torrent.poll() == None:
                    print('Process is still running')
                    time.sleep(10)
                    
                    pyautogui.press('enter')
                    send_confirmation('qBittorrent',f"qBittorrent is up and running.")

            
                
            
            for app in dict.keys():
                
                if "Openall:" in instruct :
                    application=subprocess.Popen(dict[app])
                    if application.poll()== None:
                        print("Process running succesfully")
                        send_confirmation(app,f"{app} is up and running: {app} is online!!!")
                        
                if  "Open:" in instruct :
                    application=subprocess.Popen(dict[app])
                    if application.poll()== None:
                        print("Process running succesfully")
                        send_confirmation(app,f"{app} is up and running: {app} is online!!!!")
                        
                if 'SOS' in instruct:
                    sos()

        
    # screenshot=pyautogui.screenshot()
    # screenshot.save(f"C:\\Users\\Sujay S C\\Downloads\\screen.png")
    # send_confirmation('PC','The PC is awake and the scheduled tasks are running',"C:\\Users\\Sujay S C\\Downloads\\screen.png")
             




        
    
def send_confirmation(process,body,attachment=None):
    login=email.SMTP('cleversquadtech@gmail.com','pwejkovsibyxaqfe')
    if attachment:
        login.send(to='boodelyboo1234@gmail.com',subject=f"{process} is running.",contents=body)
    else:
        login.send(to='boodelyboo1234@gmail.com',subject=f"{process} is running.",contents=body,attachments=attachment)
    login.close()
           

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
    time=datetime.datetime.now()
    kit.sendwhatmsg_instantly(phone_no='+91 6362678349',message=f'This is an SOS from Suhas ,this is his latest location https://maps.google.com/?q={latitude},{longitude} ')
        

        
get_email()
# sos()

if __name__ == '__main__':
    app.run(debug=True)
