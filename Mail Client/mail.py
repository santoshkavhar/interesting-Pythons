# you need to give gmail 3rd party access in order to send this mail from script
# python 3.6 needed for f strings
# Paste your email password in Password.txt and make it work for you.

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Our Server is gmail, to establish connection on port 25
server = smtplib.SMTP('smtp.gmail.com', 25)

# start the server
server.ehlo()

# read password
with open('Password.txt','r') as f:
	password = f.read()

# login to sender's account
server.login('skavhar1998@gmail.com', password)

# msg is a MIMEMultipart type
msg = MIMEMultipart()

# msg can be treated as a Dictionary
# we can use keys like From, To, Subject
msg['From'] = 'Santosh Kavhar'
msg['To'] = 'Santosh Kavhar'
msg['Subject'] = 'Mail Client in Python'

# Read Message
with open('Message.txt', 'r') as f:
	message = f.read()

# attach the message as plaintext
msg.attach(MIMEText(message, 'plain'))

# filename of the image attachment
filename = 'output.png'

# read image as bytes
attachment = open(filename, 'rb')

# attachment is attached to application with format of octet-stream
p = MIMEBase('application', 'octet-stream')

# attach out attchment to p
p.set_payload(attachment.read())

# encode our payload to be base64
encoders.encode_base64(p)

# add header to octet-stream, specifying attachment and filename
p.add_header('Content-Disposition', f"attachment; filename={filename}")

# attach payload to msg
msg.attach(p)

# convert msg to string
text = msg.as_string()

# send actual mail
server.sendmail('skavhar1998@gmail.com', 'santosh.kavhar@moderncoe.edu.in', text)

