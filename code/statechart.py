import sismic.model 
from pathlib import Path
from commonlog import CommonLog

class Statechart(CommonLog):
    def __init__(self, sourceFile):
        self.sourceFile = sourceFile
        self.statechart = sismic.io.import_from_yaml(filepath=sourceFile)
        assert isinstance(self.statechart, sismic.model.Statechart)
        self.targetDirectory = Path('results').joinpath(sourceFile.parts[1])
        self.targetDirectory.mkdir(parents=True, exist_ok=True)
        self.targetFile = self.targetDirectory.joinpath(sourceFile.parts[2])
        self.name = self.statechart.name
        self.complexity = 0.0
        self.isComplex = False

    def export(self):
        sismic.io.export_to_yaml(self.statechart, self.targetFile)

    def toPrintableString(self):
        mainProperties = '{:<30} {:<4} {:<4} {:.2f}'.format(self.name, len(self.statechart.states), len(self.statechart.transitions), self.complexity)
        return mainProperties
 
