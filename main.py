from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# initialize connection to our email server, we will use Outlook here
smtp = smtplib.SMTP('smtp-mail.outlook.com', port=587)

smtp.ehlo()  # send the extended hello to our server
smtp.starttls()  # tell server we want to communicate with TLS encryption

smtp.login('men_tor_ing_2023@outlook.com', 'Zoho123!')  # login to our email server

msg = MIMEMultipart() 
message = "Testing send email from python"
# setup the parameters of the message
msg['From']="men_tor_ing_2023@outlook.com"
msg['To']="orsan.awawdi@gmail.com"
msg['Subject']="This is TEST"

# add in the message body
msg.attach(MIMEText(message, 'plain'))
              
smtp.send_message(msg)
del msg