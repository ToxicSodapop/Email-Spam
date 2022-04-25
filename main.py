import smtplib, ssl
import traceback
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from time import sleep
import random
import time
from colorama import Fore, Back, Style
bright_cyan = "\033[0;96m"
red = "\033[0;31m"
print(bright_cyan+"I AM NOT RESPONSIBLE FOR HOW THIS IS USED! " + red + "IF " + Style.BRIGHT + "\033[1mYOU" + Style.RESET_ALL + " USE THIS IN A WAY THAT IT SHOULD NOT OF BEEN USED, THAT IS ON YOU.")




#dodimontini@gmail.com
#BrianTuGamer@gmail.com

def clear():
  os.system('clear')

black = "\033[97;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"

bright_white = "\033[0;97m"

time.sleep(5)
clear()
print('\n' * 3)
target = input(bright_cyan+"Target Email:  ")
message_content = input(bright_cyan+"Message for email:  ")
spam_want = input(red+"How many spam would you like to send: ")
if int(spam_want) > 100:
  print("Hey, that's too many!")
  exit()
else:
  clear()

spam_count = 0
count_time = 0
while spam_count < int(spam_want):
  clear()
  print(green+"You have sent " + red+str(spam_count) + green+' Spam out of: ' + red+str(spam_want) + green+" Spam")
  spam_count += 1
  list_name = ['bob', 'bill', 'tom', 'mike', 'wendle', 'gemmeh', 'got cash', 'meh petco', 'lasan', 'star wars', 'incredible', 'keep', 'geek', 'turbo', 'the', 'rattle', 'roll', 'I', 'Bobert', 'tommy', 'kitty', 'turtle', 'frog', 'elm', 'spam', 'annoying', 'cruel', 'overnight', 'thomas', '', 'hahafunny', 'thisisspam', 'enjoy','moo oo ah ah ah', 'whacka', 'blue', 'red' 'orange', 'incredible', 'ear']
  list_letters = ['a', 'b', 'v', 'c', 'g', 'y','r','d','e','c','t','y','u','i','p','[']
  list_numbers = ['1','2','3','4','5','6','7','8','9','10', '11','12','13','14','15','16','17','18','19','20']
  context = ssl.create_default_context()
  html = """
                  <html>
                    <body>
                      <style>
                        p {
                          font-family: impact;
                          background-color: black;
                          border_radius: 15px;
                        }
                      </style>
                      <p><strong>Bank account details</strong><br>
                      """ + message_content + """</br> 
                      </p>
                      <p><em>Bank account details</em><p>
                    </body>
                  </html>
              """
  message = MIMEMultipart("alternative")
  message["Subject"] = random.choice(list_name) + random.choice(list_letters) + random.choice(list_numbers)
  part2 = MIMEText(html, "html")
  message.attach(part2)
  try:
    to = target
    username = 'emailboi950@gmail.com'
    password = 'espammer1'
    gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_server.starttls(context=context)
    gmail_server.login(username, password)
    message["From"] = username
    message["To"] = to
  except Exception as e:
    print(e)
    print(red+"Issue!!! Spam Bot Failed!")
    gmail_server.quit()
    quit()
  def send_my_mail():  
      try:
        gmail_server.sendmail(username, to, message.as_string())
      except Exception as e:
          print("Email not sent, due to some issues.")
          gmail_server.quit()
  send_my_mail()
  if spam_want == spam_count:
      print(red+"Spamming Complete")
#filler
#filler