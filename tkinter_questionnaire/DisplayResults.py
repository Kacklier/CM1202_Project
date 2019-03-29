from tkinter import *
import shelve


class DisplayResults(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.pack()
        self.retrieveResponse()

    def retrieveResponse(self):
        countAll = 0
        countCS = 0
        countCSW = 0
        countJoints = 0
        countSE = 0
        countBIS = 0

        sumQ1All = 0.0
        sumQ2All = 0.0
        sumQ3All = 0.0

        sumP1All = 0
        sumP2All = 0
        sumP3All = 0
        sumP4All = 0
        sumP5All = 0
        sumP6All = 0

        sumQ1CS = 0.0
        sumQ2CS = 0.0
        sumQ3CS = 0.0
        sumQ1CSW = 0.0
        sumQ2CSW = 0.0
        sumQ3CSW = 0.0
        sumQ1Joints = 0.0
        sumQ2Joints = 0.0
        sumQ3Joints = 0.0
        sumQ1SE = 0.0
        sumQ2SE = 0.0
        sumQ3SE = 0.0
        sumQ1BIS = 0.0
        sumQ2BIS = 0.0
        sumQ3BIS = 0.0

        sumP1CS = 0
        sumP2CS = 0
        sumP3CS = 0
        sumP4CS = 0
        sumP5CS = 0
        sumP6CS = 0
        sumP1CSW = 0
        sumP2CSW = 0
        sumP3CSW = 0
        sumP4CSW = 0
        sumP5CSW = 0
        sumP6CSW = 0
        sumP1Joints = 0
        sumP2Joints = 0
        sumP3Joints = 0
        sumP4Joints = 0
        sumP5Joints = 0
        sumP6Joints = 0
        sumP1SE = 0
        sumP2SE = 0
        sumP3SE = 0
        sumP4SE = 0
        sumP5SE = 0
        sumP6SE = 0
        sumP1BIS = 0
        sumP2BIS = 0
        sumP3BIS = 0
        sumP4BIS = 0
        sumP5BIS = 0
        sumP6BIS = 0

        db = shelve.open('responsedb')
        respNo = len(db)

        for i in range(1, respNo + 1):
            Ans = db[str(i)]
            countAll += 1
            sumQ1All += Ans.q1
            sumQ2All += Ans.q2
            sumQ3All += Ans.q3
            sumP1All += Ans.pr1
            sumP2All += Ans.pr2
            sumP3All += Ans.pr3
            sumP4All += Ans.pr4
            sumP5All += Ans.pr5
            sumP6All += Ans.pr6

            if Ans.prog == "CS":
                countCS += 1
                sumQ1CS += Ans.q1
                sumQ2CS += Ans.q2
                sumQ3CS += Ans.q3

                sumP1CS += Ans.pr1
                sumP2CS += Ans.pr2
                sumP3CS += Ans.pr3
                sumP4CS += Ans.pr4
                sumP5CS += Ans.pr5
                sumP6CS += Ans.pr6

            if Ans.prog == "SE":
                countSE += 1
                sumQ1SE += Ans.q1
                sumQ2SE += Ans.q2
                sumQ3SE += Ans.q3

                sumP1SE += Ans.pr1
                sumP2SE += Ans.pr2
                sumP3SE += Ans.pr3
                sumP4SE += Ans.pr4
                sumP5SE += Ans.pr5
                sumP6SE += Ans.pr6

            if Ans.prog == "BIS":
                countBIS += 1
                sumQ1BIS += Ans.q1
                sumQ2BIS += Ans.q2
                sumQ3BIS += Ans.q3

                sumP1BIS += Ans.pr1
                sumP2BIS += Ans.pr2
                sumP3BIS += Ans.pr3
                sumP4BIS += Ans.pr4
                sumP5BIS += Ans.pr5
                sumP6BIS += Ans.pr6

            if Ans.prog == "Joints":
                countJoints += 1
                sumQ1Joints += Ans.q1
                sumQ2Joints += Ans.q2
                sumQ3Joints += Ans.q3

                sumP1Joints += Ans.pr1
                sumP2Joints += Ans.pr2
                sumP3Joints += Ans.pr3
                sumP4Joints += Ans.pr4
                sumP5Joints += Ans.pr5
                sumP6Joints += Ans.pr6

            if Ans.prog == "CS with":
                countCSW += 1
                sumQ1CSW += Ans.q1
                sumQ2CSW += Ans.q2
                sumQ3CSW += Ans.q3

                sumP1CSW += Ans.pr1
                sumP2CSW += Ans.pr2
                sumP3CSW += Ans.pr3
                sumP4CSW += Ans.pr4
                sumP5CSW += Ans.pr5
                sumP6CSW += Ans.pr6

        db.close

        self.txtDisplay = Text(self, height=14, width=85)
        self.txtDisplay.tag_configure('boldfont', font=('MS', 8, 'bold'))
        self.txtDisplay.tag_configure('normfont', font=('MS', 8))

        tabResults = ""
        tabResults += ("\t" + "\t" + "\t" + "\t" + "\t")
        self.txtDisplay.insert(END, "Degree Programme" + tabResults + "All" + "\t" + "CS" + "\t" "CS with" + "\t" + "BIS" + "\t" + "SE" + "\t" + "Joints" + "\n", 'boldfont')

        self.txtDisplay.insert(END, "Number of Responses:" + tabResults + str(countAll) + "\t" + str(countCS) + "\t" + str(countCSW) + "\t" + str(countBIS) + "\t" + str(countSE) + "\t" + str(countJoints) + "\n", 'normfont')

        self.txtDisplay.insert(END, "Team Experience:" + "\n", 'boldfont')

        self.txtDisplay.insert(END, "(Score: 4 = Strongly Agree to 1 = Strongly Disagree)" + "\n", 'normfont')

        if countAll > 0:
            Q1All = sumQ1All / countAll
            Q2All = sumQ2All / countAll
            Q3All = sumQ3All / countAll
        else:
            Q1All = 0
            Q2All = 0
            Q3All = 0

        if countCS > 0:
            Q1CS = sumQ1CS / countCS
            Q2CS = sumQ2CS / countCS
            Q3CS = sumQ3CS / countCS
        else:
            Q1CS = 0
            Q2CS = 0
            Q3CS = 0

        if countCSW > 0:
            Q1CSW = sumQ1CSW / countCSW
            Q2CSW = sumQ2CSW / countCSW
            Q3CSW = sumQ3CSW / countCSW
        else:
            Q1CSW = 0
            Q2CSW = 0
            Q3CSW = 0

        if countBIS > 0:
            Q1BIS = sumQ1BIS / countBIS
            Q2BIS = sumQ2BIS / countBIS
            Q3BIS = sumQ3BIS / countBIS
        else:
            Q1BIS = 0
            Q2BIS = 0
            Q3BIS = 0

        if countSE > 0:
            Q1SE = sumQ1SE / countSE
            Q2SE = sumQ2SE / countSE
            Q3SE = sumQ3SE / countSE
        else:
            Q1SE = 0
            Q2SE = 0
            Q3SE = 0

        if countJoints > 0:
            Q1Joints = sumQ1Joints / countJoints
            Q2Joints = sumQ2Joints / countJoints
            Q3Joints = sumQ3Joints / countJoints
        else:
            Q1Joints = 0
            Q2Joints = 0
            Q3Joints = 0

        self.txtDisplay.insert(END, "1. Our team worked together effectively" + tabResults + "%.1f" %Q1All + "\t %.1f"%Q1CS + "\t %.1f"%Q1CSW + "\t %.1f"%Q1BIS + "\t %.1f"%Q1SE + "\t %.1f"%Q1Joints + "\n", 'normfont')

        self.txtDisplay.insert(END, "2. Our team produced good quality products" + tabResults + "%.1f" %Q2All + "\t %.1f"%Q2CS + "\t %.1f"%Q2CSW + "\t %.1f"%Q2BIS + "\t %.1f"%Q2SE + "\t %.1f"%Q2Joints + "\n", 'normfont')

        self.txtDisplay.insert(END, "3. I enjoyed working in our team"  + tabResults + "%.1f" %Q3All + "\t %.1f"%Q3CS + "\t %.1f"%Q3CSW + "\t %.1f"%Q3BIS + "\t %.1f"%Q3SE + "\t %.1f"%Q3Joints + "\n", 'normfont')

        self.txtDisplay.insert(END, "Problems Experienced:" + "\n", 'boldfont')

        if countAll > 0:
            P1All = sumP1All * 100 / countAll
            P2All = sumP2All * 100 / countAll
            P3All = sumP3All * 100 / countAll
            P4All = sumP4All * 100 / countAll
            P5All = sumP5All * 100 / countAll
            P6All = sumP6All * 100 / countAll
        else:
            P1All = 0
            P2All = 0
            P3All = 0
            P4All = 0
            P5All = 0
            P6All = 0

        if countCS > 0:
            P1CS = sumP1CS * 100 / countCS
            P2CS = sumP2CS * 100 / countCS
            P3CS = sumP3CS * 100 / countCS
            P4CS = sumP4CS * 100 / countCS
            P5CS = sumP5CS * 100 / countCS
            P6CS = sumP6CS * 100 / countCS
        else:
            P1CS = 0
            P2CS = 0
            P3CS = 0
            P4CS = 0
            P5CS = 0
            P6CS = 0

        if countCSW > 0:
            P1CSW = sumP1CSW * 100 / countCSW
            P2CSW = sumP2CSW * 100 / countCSW
            P3CSW = sumP3CSW * 100 / countCSW
            P4CSW = sumP4CSW * 100 / countCSW
            P5CSW = sumP5CSW * 100 / countCSW
            P6CSW = sumP6CSW * 100 / countCSW
        else:
            P1CSW = 0
            P2CSW = 0
            P3CSW = 0
            P4CSW = 0
            P5CSW = 0
            P6CSW = 0

        if countBIS > 0:
            P1BIS = sumP1BIS * 100 / countBIS
            P2BIS = sumP2BIS * 100 / countBIS
            P3BIS = sumP3BIS * 100 / countBIS
            P4BIS = sumP4BIS * 100 / countBIS
            P5BIS = sumP5BIS * 100 / countBIS
            P6BIS = sumP6BIS * 100 / countBIS
        else:
            P1BIS = 0
            P2BIS = 0
            P3BIS = 0
            P4BIS = 0
            P5BIS = 0
            P6BIS = 0

        if countSE > 0:
            P1SE = sumP1SE * 100 / countSE
            P2SE = sumP2SE * 100 / countSE
            P3SE = sumP3SE * 100 / countSE
            P4SE = sumP4SE * 100 / countSE
            P5SE = sumP5SE * 100 / countSE
            P6SE = sumP6SE * 100 / countSE
        else:
            P1SE = 0
            P2SE = 0
            P3SE = 0
            P4SE = 0
            P5SE = 0
            P6SE = 0

        if countJoints > 0:
            P1Joints = sumP1Joints * 100 / countJoints
            P2Joints = sumP2Joints * 100 / countJoints
            P3Joints = sumP3Joints * 100 / countJoints
            P4Joints = sumP4Joints * 100 / countJoints
            P5Joints = sumP5Joints * 100 / countJoints
            P6Joints = sumP6Joints * 100 / countJoints
        else:
            P1Joints = 0
            P2Joints = 0
            P3Joints = 0
            P4Joints = 0
            P5Joints = 0
            P6Joints = 0

        self.txtDisplay.insert(END, "Poor Communication" + tabResults + "%d" %P1All + "% \t" + "%d" %P1CS + "% \t" + "%d" %P1CSW + "% \t" + "%d" %P1BIS + "% \t" + "%d" %P1SE + "% \t" + "%d" %P1Joints + "% \n", 'normfont')

        self.txtDisplay.insert(END, "Members Missing Meetings" + tabResults + "%d" %P4All + "% \t" + "%d" %P4CS + "% \t" + "%d" %P4CSW + "% \t" + "%d" %P4BIS + "% \t" + "%d" %P4SE + "% \t" + "%d" %P4Joints + "% \n", 'normfont')

        self.txtDisplay.insert(END, "Lack of Direction" + tabResults + "%d" %P2All + "% \t" + "%d" %P2CS + "% \t" + "%d" %P2CSW + "% \t" + "%d" %P2BIS + "% \t" + "%d" %P2SE + "% \t" + "%d" %P2Joints + "% \n", 'normfont')

        self.txtDisplay.insert(END, "Members Not Contributing" + tabResults + "%d" %P5All + "% \t" + "%d" %P5CS + "% \t" + "%d" %P5CSW + "% \t" + "%d" %P5BIS + "% \t" + "%d" %P5SE + "% \t" + "%d" %P5Joints + "% \n", 'normfont')

        self.txtDisplay.insert(END, "Disagreements Amongst Team" + tabResults + "%d" %P3All + "% \t" + "%d" %P3CS + "% \t" + "%d" %P3CSW + "% \t" + "%d" %P3BIS + "% \t" + "%d" %P3SE + "% \t" + "%d" %P3Joints + "% \n", 'normfont')

        self.txtDisplay.insert(END, "Members Not Motivated" + tabResults + "%d" %P6All + "% \t" + "%d" %P6CS + "% \t" + "%d" %P6CSW + "% \t" + "%d" %P6BIS + "% \t" + "%d" %P6SE + "% \t" + "%d" %P6Joints + "% \n", 'normfont')

        self.txtDisplay.pack()
        self.txtDisplay['state'] = DISABLED


root = Tk()
root.title("Display Results")
app = DisplayResults(root)
root.mainloop()
