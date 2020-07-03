import re

class LogParser:
    patternLst = [
        "\[\d\d:\d\d:\d\d\]",
        "<.*>.*",
        "\[WEB\].*",
        "\[Server\].*",
        "[ 가-힣A-Za-z0-9_.]*\[/[0-9.]*:[0-9]*\] logged in with entity id \d*",
        "[ 가-힣A-Za-z0-9_.]* left the game",
    ]
    delPatternLst = [
        "\[[0-9;]*m",
    ]

    def extractPattern(self, sFileLoc, sFileName, sFilePostfix):
        f = open(sFileLoc + sFileName, mode = "rt", encoding = "utf-8") 
        dest = open(sFileLoc + sFileName + sFilePostfix, mode = "w+", encoding = "utf-8")
        cntMsg = 0
        
        ln = f.readlines()

        for string in ln:
            print(string)
            for delPattern in LogParser.delPatternLst:
                string = re.sub(delPattern, '', string)  
            matchList = []
            for iPattern in LogParser.patternLst:
                pattern = re.compile(iPattern)
                foundList = pattern.findall(string)
                if len(foundList) > 0:
                    matchList.append(foundList[0])

            print(matchList)

            if len(matchList) >= 2:
                dest.write(matchList[0] + ' ' + matchList[1] + '\n')
                cntMsg += 1

        print("Parsed successfully (" + str(cntMsg) + " messages)")