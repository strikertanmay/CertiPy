import os
import sys

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from shorten import shorten 
from ..fonts import *
from ..templates import *

# Add name, institute and title to certificate
def maker( ID, name, institute, title ):
    img = Image.open("certi.png")
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
        
        img.save( '/certificates/certificates\\'+str(ID)+'.pdf', "PDF", resolution=100.0)
        return 'certificates\\'+str(ID)+'.pdf'