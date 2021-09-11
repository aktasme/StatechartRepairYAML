import sismic
from srstatechart import SRStatechart
from apcomplexdiagram import APComplexDiagram
from pathlib import Path

def createAntiPatterns():
    antiPattern = APComplexDiagram()
    antiPatterns.append(antiPattern)

antiPatterns = []
createAntiPatterns()

# Find all YAML Statechart files in data folder
for sourceFile in Path('data').rglob('*.yaml'):
    #print(path)
    statechart = sismic.io.import_from_yaml(filepath=sourceFile)
    assert isinstance(statechart, sismic.model.Statechart)

    for antiPattern in antiPatterns:
        antiPattern.control(statechart)
        #antiPattern.print()

    targetDirectory = Path('results').joinpath(sourceFile.parts[1])
    targetDirectory.mkdir(parents=True, exist_ok=True)
    targetFile = targetDirectory.joinpath(sourceFile.parts[2])
    print(targetFile)
    
    sismic.io.export_to_yaml(statechart, targetFile)

# export_to_plantuml(statechart,filepath='d:\GitHub\StatechartRepairYAML\data\simple.txt')

