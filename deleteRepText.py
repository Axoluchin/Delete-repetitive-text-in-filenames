import os


def getFiles():
    return os.listdir()


def printFiles(list):
    for file in list:
        print("- ", file)


def changeName(list, text):
    for file in list:
        os.rename(file, file.replace(text, ""))


def main():
    list = getFiles()
    print("Actual Files:")
    printFiles(list)
    text = input("Insert text to delete in files: \n")
    changeName(list,text)
    list = getFiles()
    print("New Files:")
    printFiles(list)
