class CommonLog:
    def __init__(self):
        self.printableString = ""

    def toPrintableString(self):
        return ""

    def toPlusMinusString(self, condition):
        plusMinusString = '-'
        if condition == True:
            plusMinusString = '+'
        return plusMinusString

    def print(self):
        print(self.toPrintableString())    