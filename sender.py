import xlrd
import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Meant to convert full names to abbreviations
def shorten( text, _max ):
    t = text.split(" ")
    text = ''
    if len(t)>1:
        for i in t[:-1]:
            text += i[0] + '.'
    text += ' ' + t[-1]
    if len(text) < _max :
        return text
    else :
        return -1

# Add name, institute and project to certificate
def make_certi( ID, name, institute, topic ):
    img = Image.open("group1.png")
    draw = ImageDraw.Draw(img)
    # Load font
    font = ImageFont.truetype("RobotoCondensed-Regular.ttf", 70)
    font2 = ImageFont.truetype("RobotoCondensed-Regular.ttf", 60)
    font1 = ImageFont.truetype("RobotoCondensed-Regular.ttf", 90)

    # Check sizes and if it is possible to abbreviate
    # if not the IDs are added to an error list
    if ( len( name ) > 30 ):
        name = shorten( name, 30 )
    if ( len( institute ) > 60 ):
        institute = shorten( institute, 60 )
    if ( len( topic ) > 20 ):
        topic = shorten( topic, 20 )

    if name == -1 or topic == -1 or institute == -1 :
        return -1
    else:
        # Insert text into image template
        draw.text( (1730, 1160), name, (64,64,64), font=font1 )
        draw.text( (720, 1280), institute, (64,64,64), font=font2 )
        draw.text( (930, 1375), topic, (64,64,64), font=font )

        if not os.path.exists( 'certificates' ) :
            os.makedirs( 'certificates' )

        # Save as a PDF
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        img.save( 'certificates\\'+str(ID)+'.pdf', "PDF", resolution=100.0)
        return 'certificates\\'+str(ID)+'.pdf'

# Email the certificate as an attachment
def email_certi( filename, receiver ):
    username = ""
    password = ""
    sender = username + '@gmail.com'

    msg = MIMEMultipart()
    msg['Subject'] = 'Aparoksha Techtour Certificate'
    msg['From'] = username +'@gmail.com'
    msg['Reply-to'] = username + '@gmail.com'
    msg['To'] = receiver

    # That is what u see if dont have an email reader:
    msg.preamble = 'Multipart massage.\n'
    
    # Body
    part = MIMEText( "Hello,\n\nPlease find attached your Aparoksha Techtour certificate.\n\nGreetings." )
    msg.attach( part )

    # Attachment
    part = MIMEApplication(open(filename,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename = os.path.basename(filename))
    msg.attach( part )

    # Login
    server = smtplib.SMTP( 'smtp.gmail.com:587' )
    server.starttls()
    server.login( username, password )

    # Send the email
    server.sendmail( msg['From'], msg['To'], msg.as_string() )
   

if __name__ == "__main__":
    error_list = []
    error_count = 0

    os.chdir(os.path.dirname(os.path.abspath((sys.argv[0]))))

    # Read data from an excel sheet from row 2
    Book = xlrd.open_workbook('List.xlsx')
    WorkSheet = Book.sheet_by_name('Sheet1')
    
    num_row = WorkSheet.nrows - 1
    row = 0

    while row < num_row:
        row += 1
        
        ID = WorkSheet.cell_value( row, 0 )
        name = WorkSheet.cell_value( row, 1 )
        institute = WorkSheet.cell_value( row, 2 )
        receiver = WorkSheet.cell_value( row, 3 )
        topic = WorkSheet.cell_value( row, 4 )
        
        # Make certificate and check if it was successful
        filename = make_certi( ID, name, institute, topic )
        
        # Successfully made certificate
        if filename != -1:
            email_certi( filename, receiver )
            print ("Sent to" + ID) 
        # Add to error list
        else:
            error_list.append( ID )
            error_count += 1

    # Print all failed IDs
    print (str(error_count) + " Errors- List:" + ','.join(error_list))
