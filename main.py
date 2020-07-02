import os
import logParser

filePostfix = "_parse.txt"

def getFileList():
    path = "./"
    allFileList = os.listdir(path)
    fileList = [file for file in allFileList if file.endswith(".log")]

    print ("log file list: {}".format(fileList))
    return fileList

def main():
    fileList = getFileList()

    parser = logParser.LogParser()
    for logFile in fileList:
        print("parsing " + logFile)
        parser.extractPattern("", logFile, filePostfix)

if __name__ == '__main__':
    main()