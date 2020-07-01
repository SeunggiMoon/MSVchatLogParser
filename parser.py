import re

fileLoc = "C:/Users/Moon/Documents/Logs/"
fileName = "test.log"
filePostfix = "_parse.txt"

patternLst = [
    "\[\d\d:\d\d:\d\d\]",
    "<.*>.*",
    "\[WEB\].*"
]

delPatternLst = [
    "\[[0-9;]*m"
]

class LogParser:
    def extractPattern(self, sFileLoc, sFileName, sFilePostfix, sPatternLst, sDelPatternLst):
        cntMsg = 0
        f = open(sFileLoc + sFileName, mode = "rt", encoding = "utf-8") 
        dest = open(sFileLoc + sFileName + sFilePostfix, mode = "w+", encoding = "utf-8")
        
        ln = f.readlines()

        for string in ln:
            for delPattern in sDelPatternLst:
                string = re.sub(delPattern, '', string)
            print(string)
            matchList = []
            for iPattern in sPatternLst:
                pattern = re.compile(iPattern)
                foundList = pattern.findall(string)
                if len(foundList) > 0:
                    matchList.append(foundList[0])

            print(matchList)

            if len(matchList) >= 2:
                dest.write(matchList[0] + ' ' + matchList[1] + '\n')
                cntMsg += 1

        print("Parsed successfully (" + str(cntMsg) + " messages)")

parser = LogParser()
parser.extractPattern(fileLoc, fileName, filePostfix, patternLst, delPatternLst)