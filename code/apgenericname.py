from antipatternbase import AntiPatternBase
from statechart import Statechart
import Levenshtein

class APGenericName(AntiPatternBase):
    def __init__(self):
        AntiPatternBase.__init__(self, __class__.__name__)

    def control(self, statechart: Statechart):
        bReturn = False

        for state in statechart.statechart.states:           
            distance = Levenshtein.distance("state_", state)
            if distance <= 3:
                self.repair(statechart, state)
                self.hitCountState += 1
                bReturn = True

        if bReturn:
            self.hitCountStatechart += 1
            statechart.hasGenericName = True
        
        return bReturn

    def repair(self, statechart: Statechart, stateString):
        state = statechart.statechart.state_for(stateString)
        inTransitions = statechart.statechart.transitions_to(stateString)

        if state.isDefault:
            parentStateString = statechart.statechart.parent_for(stateString)
            newStateNameString = parentStateString + '_Initial'
            statechart.statechart.rename_state(stateString, newStateNameString)
        elif inTransitions:
            firstTransition = inTransitions[0]
            firstTransitionSourceStateString = firstTransition.source
            newStateNameString = firstTransitionSourceStateString + '_' + firstTransition.event
            statechart.statechart.rename_state(stateString, newStateNameString)
        else:
            print('No automatic repairing')

            