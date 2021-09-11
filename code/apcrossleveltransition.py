from antipatternbase import AntiPatternBase
from statechart import Statechart

class APCrossLevelTransition(AntiPatternBase):
    def __init__(self):
        self.name = __class__.__name__

    def control(self, statechart: Statechart):
        bReturn = False

        for transition in statechart.statechart.transitions:
            print(transition)
            print(transition.source)

        return bReturn
