import commonlog
from statechart import Statechart

class AntiPatternBase(commonlog.CommonLog):
    def __init__(self):
        self.name = ""

    def control(statechart: Statechart):
        return False

    def repair(statechart: Statechart):
        return False

    def toPrintableString(self):
        return 'AntiPattern: {}'.format(self.name)