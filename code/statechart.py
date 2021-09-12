import sismic.model 
from pathlib import Path
from commonlog import CommonLog

class Statechart(CommonLog):
    def __init__(self, sourceFile):
        CommonLog.__init__(self)
        self.sourceFile = sourceFile
        self.statechart = sismic.io.import_from_yaml(filepath=sourceFile)
        assert isinstance(self.statechart, sismic.model.Statechart)
        self.targetDirectory = Path('results').joinpath(sourceFile.parts[1])
        self.targetDirectory.mkdir(parents=True, exist_ok=True)
        self.targetFile = self.targetDirectory.joinpath(sourceFile.parts[2])
        self.name = self.statechart.name
        
        self.complexity = 0.0
        self.isComplex = False
        self.hasCrossLevelTransition = False
        self.hasMissingEvent = False
        self.hasGenericName = False


    def export(self):
        sismic.io.export_to_yaml(self.statechart, self.targetFile)

    def toPrintableString(self):
        mainProperties = '{:<30} {:<4} {:<4} {:.2f}'.format(self.name, len(self.statechart.states), len(self.statechart.transitions), self.complexity)
        antiPatternProperties = ' | {}'.format(CommonLog.toPlusMinusString(self, self.hasCrossLevelTransition))
        antiPatternProperties += ' {}'.format(CommonLog.toPlusMinusString(self, self.hasMissingEvent))
        antiPatternProperties += ' {}'.format(CommonLog.toPlusMinusString(self, self.hasGenericName))
        return mainProperties + antiPatternProperties
 
