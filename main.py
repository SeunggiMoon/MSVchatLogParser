import os
import logParser

def main():
    fileLoc = "C:/Users/Moon/Documents/Logs/"
    fileName = "2016-03-03-5(2).log"
    filePostfix = "_parse.txt"

    parser = logParser.LogParser()
    parser.extractPattern(fileLoc, fileName, filePostfix)

if __name__ == '__main__':
    main()