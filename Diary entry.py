#Program to write a diary entry
# import module to add current date/time timestamp
#exception added to catch IOerror

from datetime import datetime

current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
str_current_datetime = str(current_datetime)


try:
    file=open("Diary.txt","W")
except FileNotFoundError:
    print("The file was not found")

file.write("str_current_datetime. Diary entry text")
file.close()

#Program to read previous diary entries
try:
    file=open("Diary.txt","r")
except FileNotFoundError:
    print("The file was not found")
out=file.read()
file.close()