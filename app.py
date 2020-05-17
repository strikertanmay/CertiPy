import xlrd
import smtplib
import os
import sys

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from config.credentials import *
from func.sender import sender
from func.maker import maker

def put_data():
    error_list = []
    error_count = 0

    # Read data from an excel sheet from row 2
    abspath = os.path.abspath("")
    data_dir = os.path.join(abspath, "data")
    Book = xlrd.open_workbook(f'{data_dir}/data.xlsx')
    WorkSheet = Book.sheet_by_name('Sheet1')
    
    num_row = WorkSheet.nrows - 1
    row = 0

    while row < num_row:
        row += 1
        
        ID = WorkSheet.cell_value( row, 0 )
        name = WorkSheet.cell_value( row, 1 )
        institute = WorkSheet.cell_value( row, 2 )
        receiver = WorkSheet.cell_value( row, 3 )
        title = WorkSheet.cell_value( row, 4 )
        
        # Make certificate and check if it was successful
        filepath , filename = maker( ID, name, institute, title )
        
        # Successfully made certificate
        if filepath != -1:
            sender( filepath, filename, receiver )
            print ("Sent to " + ID) 
        # Add to error list
        else:
            error_list.append( ID )
            error_count += 1

    # Print all failed IDs
    print (str(error_count) + " Errors- List:" + ','.join(error_list))

if __name__ == "__main__":
    put_data()