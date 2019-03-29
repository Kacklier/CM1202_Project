#Author: Wojtek
class Test:
    def __init__(self, testNo=0, title="", testType="", duration=0, chkDates=0, startDate="", endDate="", **kwargs):
        self.testNo = testNo
        self.title = title
        self.testType = testType
        self.duration = duration
        self.chkDates = chkDates
        self.startDate = startDate
        self.endDate = endDate
        for key, value in kwargs.items():
            self.key = value
