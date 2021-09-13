from sismic.model.elements import Transition
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
                                
            if not isRoot and bTransitionsEmpty and not state.on_entry and not state.on_exit and inTransitions and outTransitions:
                self.repair(statechart, state, inTransitions, outTransitions)
                self.hitCountState += 1
                bReturn = True

        if bReturn:
            self.hitCountStatechart += 1
            statechart.hasIsolatedState = True
        
        return bReturn

    def repair(self, statechart: Statechart, state, inTransitions, outTransitions):
        for inTransition in inTransitions:
            for outTransition in outTransitions:
                sourceState = inTransition.source
                targetState = outTransition.target
                newTransition = Transition(sourceState, targetState)
                statechart.statechart.add_transition(newTransition)
                statechart.statechart.remove_transition(inTransition)
                statechart.statechart.remove_transition(outTransition)
                statechart.statechart.remove_state(state.name)

    def isTransitionsEmpty(self, statechart: Statechart, transitions):
        bReturn = True
        for transition in transitions:
            if transition.event or transition.guard or transition.action:
                bReturn = False
                break
        
        return bReturn