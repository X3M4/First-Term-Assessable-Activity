"""This file will make the backup easier. In the case the user OS was a Windows or Linux System,
and the folder which the user wants to backup  is in the same directory as the script, the user has just write
the name of the folder to the backup.

In the case the folder which the user wants to backup is in other place in the hard drive, if the user System is running on Windows,
the user will have to write C:\ follows the path of the folder to the backup. 

In the case the user Linux System, the user will have to write / follows the path of the folder to the backup."""

#package needed for working with dates.
import datetime
#package needed for send commands to console
import subprocess

#This function builds the filename + extension of the file.
def backup(filename, file):
    filename = filename
    file = file
    #this line creates an object date with the current date
    date = datetime.datetime.now()
    #This line transform the var date into a format string with the date.
    date = date.strftime('%Y-%m-%d-%H-%M-%S')
    #This line adds the .zip extension to the filename.
    filename = filename + str(date) + file
    #Thia line returns the complete filename
    return filename

#In this line the user writes the folder path.
data_folder = input("Please, enter a folder or file route for making a data backup\n")
#This var creates a var with an object subproccess to compress the folder in a zip file.
data_zip = subprocess.run(["zip", "-r", "-q", backup("Backup", ".zip"), data_folder])
