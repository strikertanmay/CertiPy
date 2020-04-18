# CertiPy
A python script that will generate certificates of events and send mail to the participants just by giving an excel sheet and a certificate template image as an input.

## How To Use

- Put certificate template image in templates folder and excel sheet in data folder.
- Put your mail credentials in credentials.py file which is in config folder.
- Adjust the text position, font-style and font-size in maker.py file which is in func folder.

## How To Run
```
 pip install -r requirements.txt
 python app.py
```
### Note
If there is any problem occured while sending mail, just check that you have enable less secure apps on your gmail account from which you are trying to send the mails.
