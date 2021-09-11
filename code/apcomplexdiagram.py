from antipatternbase import AntiPatternBase
from srstatechart import SRStatechart

class APComplexDiagram(AntiPatternBase):
    def __init__(self):
        self.name = __class__.__name__
        self.COMPLEXITY_THRESHOLD = 2.0
        self.complexity = 0.0

    def control(self, statechart: SRStatechart):
        print('{} #S:{} #T:{}'.format(statechart.name, len(statechart.states), len(statechart.transitions))) 