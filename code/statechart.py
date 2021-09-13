import sismic.model
import sismic.io
import subprocess
from pathlib import Path
from commonlog import CommonLog

class Statechart(CommonLog):
    def __init__(self, sourceFile):
        CommonLog.__init__(self)
        self.sourceFile = sourceFile
        self.sorcePlantumlFile = str(sourceFile) + '.plant'
        self.statechart = sismic.io.import_from_yaml(filepath=sourceFile)
        assert isinstance(self.statechart, sismic.model.Statechart)
        self.targetDirectory = Path('results').joinpath(sourceFile.parts[1])
        self.targetDirectory.mkdir(parents=True, exist_ok=True)
        self.targetFile = self.targetDirectory.joinpath(sourceFile.parts[2])
        self.targetPlantumlFile = str(self.targetFile) + '.plant'
        self.name = self.statechart.name

        sismic.io.export_to_plantuml(self.statechart, self.sorcePlantumlFile)
        subprocess.call(['java', '-jar', 'plantuml.jar', self.sorcePlantumlFile])
        
        self.hasCrossLevelTransition = False
        self.hasMissingEvent = False
        self.hasGenericName = False
        self.hasUnreachableState = False
        self.hasCascadedCondition = False
        self.hasIsolatedState = False
        self.isComplex = False
        self.complexity = 0.0

        self.initialize()

    def initialize(self):
        for stateString in self.statechart.states:
            state = self.statechart.state_for(stateString)
            state.isRoot = False
            state.isDefault = False

        root = self.statechart.state_for(self.statechart.root)
        root.isRoot = True

        for stateString in self.statechart.states:
            state = self.statechart.state_for(stateString)
            if isinstance(state, sismic.model.CompoundState) and state.initial:
                initialState = self.statechart.state_for(state.initial)
                initialState.isDefault = True

        for stateString in self.statechart.states:
            state = self.statechart.state_for(stateString)

    def export(self):
        sismic.io.export_to_yaml(self.statechart, self.targetFile)
        sismic.io.export_to_plantuml(self.statechart, self.targetPlantumlFile)
        subprocess.call(['java', '-jar', 'plantuml.jar', self.targetPlantumlFile])

    def toPrintableString(self):
        mainProperties = '{:<30} {:<4} {:<4} {:.2f}'.format(self.name, len(self.statechart.states), len(self.statechart.transitions), self.complexity)
        antiPatternProperties = ' | {}'.format(CommonLog.toPlusMinusString(self, self.hasCrossLevelTransition))
        antiPatternProperties += ' {}'.format(CommonLog.toPlusMinusString(self, self.hasMissingEvent))
        antiPatternProperties += ' {}'.format(CommonLog.toPlusMinusString(self, self.hasGenericName))
        antiPatternProperties += ' {}'.format(CommonLog.toPlusMinusString(self, self.hasUnreachableState))
        antiPatternProperties += ' {}'.format(CommonLog.toPlusMinusString(self, self.hasCascadedCondition))
        antiPatternProperties += ' {}'.format(CommonLog.toPlusMinusString(self, self.hasIsolatedState))
        antiPatternProperties += ' {}'.format(CommonLog.toPlusMinusString(self, self.isComplex))
        return mainProperties + antiPatternProperties
 
