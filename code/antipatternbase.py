import commonlog
from statechart import Statechart

class AntiPatternBase(commonlog.CommonLog):
    def __init__(self, name):
        self.name = name
        self.hitCountStatechart = 0
        self.hitCountTransition = 0
        self.hitCountState = 0

    def control(self, statechart: Statechart):
        return False

    def repair(self, statechart: Statechart):
        return False

    def toPrintableString(self):
        return 'AntiPattern: {}'.format(self.name)