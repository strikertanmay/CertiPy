import smtplib

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

# Email the certificate as an attachment
def sender( filename, receiver ):
    username = user_mail
    password = mail_password
    sender = username + '@gmail.com'

    msg = MIMEMultipart()
    msg['Subject'] = 'Subject'
    msg['From'] = username +'@gmail.com'
    msg['Reply-to'] = username + '@gmail.com'
    msg['To'] = receiver
    msg.preamble = 'Multipart massage.\n'
    
    # Body
    part = MIMEText( "Greetings Text" )
    msg.attach( part )

    # Attachment
    part = MIMEApplication(open(filename,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename = os.path.basename(filename))
    msg.attach( part )

    server = smtplib.SMTP( 'smtp.gmail.com:587' )
    server.starttls()
    server.login( username, password )
    server.sendmail( msg['From'], msg['To'], msg.as_string() )
   