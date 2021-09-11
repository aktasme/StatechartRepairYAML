from antipatternbase import AntiPatternBase
from statechart import Statechart

class APComplexDiagram(AntiPatternBase):
    def __init__(self):
        self.name = __class__.__name__
        self.COMPLEXITY_THRESHOLD = 2.0
        self.complexity = 0.0

    def control(self, statechart: Statechart):
        bReturn = False
        statechart.complexity= len(statechart.statechart.transitions) / len(statechart.statechart.states)

        if statechart.complexity >= self.COMPLEXITY_THRESHOLD:
            bReturn = True
            statechart.isComplex = True

        return bReturn
            