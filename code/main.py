import sismic.io
import sismic.model
from statechart import Statechart
from apcomplexdiagram import APComplexDiagram
from apcrossleveltransition import APCrossLevelTransition
from pathlib import Path

def createAntiPatterns():
    antiPattern = APComplexDiagram()
    antiPatterns.append(antiPattern)

    antiPattern = APCrossLevelTransition()
    antiPatterns.append(antiPattern)


antiPatterns = []
createAntiPatterns()

# Find all YAML Statechart files in data folder
for sourceFile in Path('data').rglob('*.yaml'):
    statechart = Statechart(sourceFile)

    for antiPattern in antiPatterns:
        antiPattern.control(statechart)
        #antiPattern.print()

    # Print formatted statechart results
    statechart.print()
    statechart.export()

# export_to_plantuml(statechart,filepath='d:\GitHub\StatechartRepairYAML\data\simple.txt')

