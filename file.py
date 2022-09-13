from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime
import time
from email.message import EmailMessage
import ssl
import smtplib

maile = {'Tymek':'tymdyb@gmail.com',
          'Dawid':'tymdyb@gmail.com',
          'Michał':'tymdyb@gmail.com',
          'Kuba':'tymdyb@gmail.com',
          'Norbert':'tymdyb@gmail.com',
          'Maks':'ekran.coek@gmail.com',
          'Maciek':'tymekdybal@gmail.com'
}
#asldfkjaslfjkd
#initialize calendar api
scopes = ['https://www.googleapis.com/auth/calendar']
credentials = pickle.load(open('token.txt', "rb"))
service = build("calendar", "v3", credentials=credentials )
result = service.events().list(calendarId='sprawdzacz12@gmail.com').execute()

#initialize mail sending
email_sender = 'sprawdzacz12@gmail.com'
email_password = 'demnykageifuhjln'
subject = 'Wyświetlanie coek'
body = "Hej, jesteś w grafiku na dzisiejszą niedzielę."
em = EmailMessage()
em['From'] = email_sender
em['Subject'] = subject
context = ssl.create_default_context()



def send_mail():
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)

today = datetime.today().strftime("%Y/%m/%d")
today_day_of_week = datetime.today().strftime("%A")
for i in result['items']:
  start = i['start']['date']
  end = i['end']['date']

  start = start.replace('-','/')
  end = end.replace('-', '/')

  if today > start and today < end and today_day_of_week=='Tuesday':
    print(i['summary'])
    current_event = i
    name = current_event['summary']
    first = ''
    second = ''
    third = ''
    name = name.split(' - ')
    second = name[-2].split(',')[0]
    first = name[0]
    third = name[-1]
    print(first+'\n' + second + '\n' + third)
    
    body +="\n" +current_event['summary'].replace(', ', '\n')
    receivers = [maile[first], maile[second], maile[third]]
    em['To'] = ", ".join(receivers)
    print(body)
    em.set_content(body)
    send_mail()

today = datetime.today().strftime("%Y/%m/%d")




#converted_start = time.strptime(start, "%d/%m/%Y")
#converted_end = time.strptime(end, "%d/%m/%Y")

#print(converted_start)

