import datetime
import os
from posixpath import expanduser
import time

curr_time = time.strftime("DATE=%d-%m-%Y TIME=%I %p") #Gives current time in 12 hr format as a str
home = expanduser("~") #Gives the default home directory
#     filename = f"{home}\\Documents\\Attendance\\Attendance {curr_time}.csv"#Creates a .csv file with current date and time
filename = f"{home}\\Documents\\Attendance\\Attendance {curr_time}.csv"
# print(filename)

folderPath = f"{home}\\Documents\\Attendance"#Default folder path
if not os.path.exists(folderPath):#Checks if folder exists or not. If not then create one
        os.makedirs(f"{home}\\Documents\\Attendance")

with open(filename, 'a'):
    with open(filename, 'r+') as f:
        # myFile_Data = f.readlines()# To read all the lines in the files at once
        nameInFile = []
        # for line in myFile_Data:
        #     entry = line.split(',')
        #     nameInFile.append(entry[0])
        # if name not in nameInFile:
        #     current_time = datetime.now()
        #     dtString = current_time.strftime('%I:%M:%S')
        #     f.writelines(f'{name},{dtString}\n')