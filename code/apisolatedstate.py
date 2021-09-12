from antipatternbase import AntiPatternBase
from statechart import Statechart

class APIsolatedState(AntiPatternBase):
    def __init__(self):
        AntiPatternBase.__init__(self, __class__.__name__)
        self.transitionsFound = []

    def control(self, statechart: Statechart):
        bReturn = False

        for stateString in statechart.statechart.states:
            state = statechart.statechart.state_for(stateString)
            isRoot = state.isRoot
            inTransitions = statechart.statechart.transitions_to(stateString)
            outTransitions = statechart.statechart.transitions_from(stateString)
            bTransitionsEmpty = self.isTransitionsEmpty(statechart, inTransitions + outTransitions)
                                
            if not isRoot and bTransitionsEmpty and not state.on_entry and not state.on_exit:
                self.hitCountState += 1
                bReturn = True

        if bReturn:
            self.hitCountStatechart += 1
            statechart.hasIsolatedState = True
        
        return bReturn

    def isTransitionsEmpty(self, statechart: Statechart, transitions):
        bReturn = False
        for transition in transitions:
            if not transition.event and not transition.guard and not transition.action:
                bReturn = True
        
        return bReturn
