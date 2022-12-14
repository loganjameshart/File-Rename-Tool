import os, csv

#get current directory
directory = input(r"Please input directory.")
os.chdir(directory)

#get CSV file you're using
fileName = input("What is the filename?")

#create CSV object, get data as list
with open(fileName, "r") as fileObject:
    fileReader = csv.reader(fileObject)
    fileData = list(fileReader) 
    for column1, column2 in fileData:
        os.rename(directory+"\\"+column1, directory+"\\"+column2)

print("Renaming complete.")
