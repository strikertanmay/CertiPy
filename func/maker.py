import os
import sys

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from func.shorten import shorten 


# Add name, institute and title to certificate
def maker( ID, name, institute, title ):
    abspath = os.path.abspath("")
    templates_dir = os.path.join(abspath, "templates")
    img = Image.open(f'{templates_dir}/certi.png')
    draw = ImageDraw.Draw(img)

    # Load font
    fonts_dir = os.path.join(abspath, "fonts")
    font = ImageFont.truetype(f"{fonts_dir}/RobotoCondensed-Regular.ttf", 70)
    font2 = ImageFont.truetype(f"{fonts_dir}/RobotoCondensed-Regular.ttf", 60)
    font1 = ImageFont.truetype(f"{fonts_dir}/RobotoCondensed-Regular.ttf", 90)

    # Check sizes and if it is possible to abbreviate
    if ( len( name ) > 20 ):
        name = shorten( name, 20 )
    if ( len( institute ) > 50 ):
        institute = shorten( institute, 50 )
    if ( len( title ) > 15 ):
        title = shorten( title, 15 )

    if name == -1 or title == -1 or institute == -1 :
        return -1
    else:
        # Insert text into image template
        draw.text( (1730, 1160), name, (64,64,64), font=font1 )
        draw.text( (720, 1280), institute, (64,64,64), font=font2 )
        draw.text( (930, 1375), title, (64,64,64), font=font )

        main_dir = os.path.join(abspath, "certificates")
        if not os.path.isdir(main_dir) :
            os.makedirs(main_dir)

        # Save as a PDF
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        img.save( f'{main_dir}/certificate\\'+str(ID)+'.pdf', "PDF", resolution=100.0)
        return  f'{main_dir}/certificate\\' + str(ID)+ '.pdf' , 'certificate\\' + str(ID) + '.pdf'