import csv
from tkinter import *

"""
******use this function to get correct answer list

correctAnsLst=[]

def read_csv_data(filename):
    with open (filename) as csv_file:
        reader = csv.reader(csv_file)
        a=[]
        for row in reader:
            if row[2]=="1":
                a.append(row)
        for i in a:
            correctAns = i[0].strip("answer")
            correctAnsLst.append(int(correctAns))
    return correctAnsLst
"""

"""
******because i cant find those two csv file, temp list here
"""
correctAnsLst=[2,3,4,1]
studentResult=[[2,3,4,1],[2,1,3,5],[1,2,3,4],[2,3,4,5],[2,3,4,2],[1,2,3,4],[1,3,2,2],[2,3,3,3],[2,3,1,4],[2,4,1,3]]


"""
******************
"""

answerDict={}
def getAnswerDict(correctAnsLst,studentResult):
    for n in range(0, len(correctAnsLst)):
        answerDict[n+1]=0
        for i in studentResult:
            if i[n] == correctAnsLst[n]:
                answerDict[n+1]+=1
    return answerDict

getAnswerDict(correctAnsLst,studentResult)
print(answerDict)

totalMark=[]
studentNum=[]
def generateTotalMark(correctAnsLst,studentResult):
    totalMark.append(len(correctAnsLst))
    studentNum.append(len(studentResult))
    return totalMark,studentNum

generateTotalMark(correctAnsLst,studentResult)
print(totalMark,studentNum)

percentageDict={}

for i in answerDict:
    print(answerDict[i])

print(round(2/9,2)*100,"%")

class statisticsPage(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.createStatisticsPage()

    def createStatisticsPage(self):
        pass


root = Tk()
root.title("Statistics Page")
app = statisticsPage(root)
root.mainloop()
