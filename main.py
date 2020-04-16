import xlrd
import smtplib
import os
import sys

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from config.credentials import *


if __name__ == "__main__":
    print(os.path.abspath("main.py"))
    # error_list = []
    # error_count = 0

    # os.chdir(os.path.dirname(os.path.abspath((sys.argv[0]))))

    # # Read data from an excel sheet from row 2
    # Book = xlrd.open_workbook('List.xlsx')
    # WorkSheet = Book.sheet_by_name('Sheet1')
    
    # num_row = WorkSheet.nrows - 1
    # row = 0

    # while row < num_row:
    #     row += 1
        
    #     ID = WorkSheet.cell_value( row, 0 )
    #     name = WorkSheet.cell_value( row, 1 )
    #     institute = WorkSheet.cell_value( row, 2 )
    #     receiver = WorkSheet.cell_value( row, 3 )
    #     topic = WorkSheet.cell_value( row, 4 )
        
    #     # Make certificate and check if it was successful
    #     filename = make_certi( ID, name, institute, topic )
        
    #     # Successfully made certificate
    #     if filename != -1:
    #         email_certi( filename, receiver )
    #         print ("Sent to" + ID) 
    #     # Add to error list
    #     else:
    #         error_list.append( ID )
    #         error_count += 1

    # # Print all failed IDs
    # print (str(error_count) + " Errors- List:" + ','.join(error_list))
