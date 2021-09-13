from antipatternbase import AntiPatternBase
from statechart import Statechart

class APCrossLevelTransition(AntiPatternBase):
    def __init__(self):
        AntiPatternBase.__init__(self, __class__.__name__)

    def control(self, statechart: Statechart):
        bReturn = False

        for transition in statechart.statechart.transitions:
            sourceDepth = statechart.statechart.depth_for(transition.source)
            targetDepth = statechart.statechart.depth_for(transition.target)

            if sourceDepth - targetDepth == 1:
                self.repair(statechart, transition)
                bReturn = True
                self.hitCountTransition += 1
        
        if bReturn == True:
            self.hitCountStatechart += 1
            statechart.hasCrossLevelTransition = True
        
        return bReturn

    def repair(self, statechart: Statechart, transition):
        sourceParentString = statechart.statechart.parent_for(transition.source)
        statechart.statechart.rotate_transition(transition, new_source=sourceParentString)         
        
