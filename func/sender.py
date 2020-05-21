import smtplib
import os
import logging

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from config.credentials import *


# Email the certificate as an attachment
def sender( filepath, filename, receiver ):
    username = user_mail
    password = mail_password

    msg = MIMEMultipart()
    msg['Subject'] = 'Subject'
    msg['From'] = username
    msg['Reply-to'] = username
    msg['To'] = receiver
    msg.preamble = 'Multipart massage.\n'
    
    # Body
    part = MIMEText( "Mail body content" )
    msg.attach( part )

    # Attachment
    part = MIMEApplication(open(filepath,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filepath = os.path.basename(filepath), filename=filename)
    msg.attach( part )

    try:
        server = smtplib.SMTP( 'smtp.gmail.com:587' )
        server.starttls()
        server.login( username, password )
        server.sendmail( msg['From'], msg['To'], msg.as_string() )
        return 1
    except Exception as e:
        logging.error(e)
        return 0
   