from antipatternbase import AntiPatternBase
from statechart import Statechart

class APUnreachableState(AntiPatternBase):
    def __init__(self):
        AntiPatternBase.__init__(self, __class__.__name__)
        self.transitionsFound = []

    def control(self, statechart: Statechart):
        bReturn = False

        for stateString in statechart.statechart.states:
            state = statechart.statechart.state_for(stateString)
            isRoot = state.isRoot
            isDefault = state.isDefault
            inTransitions = statechart.statechart.transitions_to(stateString)                   
            if not isRoot and not isDefault and not inTransitions:
                self.hitCountState += 1
                bReturn = True

        if bReturn:
            self.hitCountStatechart += 1
            statechart.hasUnreachableState = True
        
        return bReturn
