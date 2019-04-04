import csv
from tkinter import *




def openS():
    root = Toplevel()
    root.title("Statistics Page")
    app=statisticsPage(root)
    root.mainloop()
"""
******use this function to get correct answer list

correctAnsLst=[]

def read_assessment_csv_data(filename):
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
studentResult=[[2,3,4,1],[2,1,3,5],[1,2,3,4],[2,3,4,5],[2,3,4,2],[1,2,3,4],[1,3,2,2],[2,3,3,3],[2,3,1,4],[2,4,1,3],[2,1,2,1]]


"""
******************
"""


answerDict={}
def getAnswerDict(correctAnsLst,studentResult):
    for n in range(0, len(correctAnsLst)):
        answerDict[n+1]=0
        for i in studentResult:
            if i[n]==correctAnsLst[n]:
                answerDict[n+1]+=1
    return answerDict

getAnswerDict(correctAnsLst,studentResult)

totalMark=[]
studentNum=[]
def generateTotalMark(correctAnsLst,studentResult):
    totalMark.append(len(correctAnsLst))
    studentNum.append(len(studentResult))
    return totalMark,studentNum

generateTotalMark(correctAnsLst,studentResult)

percentageDict={}

def generatePercentage(correctAnsLst,answerDict,studentNum):
    for n in range(0, len(correctAnsLst)):
        percentageDict[n+1]=[]
        for i in answerDict:
            if (i-1)==n:
                floatNum=int(answerDict[i])/studentNum[0]
                finalNum=round(round(floatNum, 2)*100,1)
                percentageDict[n+1].append(finalNum)
    return percentageDict

generatePercentage(correctAnsLst,answerDict,studentNum)

MinLst=[]
def getMin(percentageDict):
    tempLst=[]
    for key,value in percentageDict.items():
        tempLst.append(int(value[0]))
    Ans=min(tempLst)
    for key,value in percentageDict.items():
        if int(value[0])==Ans:
            MinLst.append(key)
    return MinLst
    

getMin(percentageDict)

class statisticsPage(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.createStatisticsPage()

    def createStatisticsPage(self):
        titleLabel=Label(self,text="Statistics Page",font=("MS",20,"bold"))
        titleLabel.pack()

        for key,value in percentageDict.items():
            QLabel=Label(self,text="Q No."+str(key)+": "+str(value[0])+"%",font=("MS",15,"bold"))
            QLabel.pack()

        qustionMostIncoLabel=Label(self,text="The question most often answered incorrectly: Q No."+str(MinLst[0]),font=("MS",15,"bold"))
        qustionMostIncoLabel.pack()

        studentNumLabel=Label(self,text="Number of attempts at the test:"+str(studentNum[0]),font=("MS",15,"bold"))
        studentNumLabel.pack()

