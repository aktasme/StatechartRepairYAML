import sismic.io
import sismic.model
from statechart import Statechart
from apcrossleveltransition import APCrossLevelTransition
from apmissingevent import APMissingEvent
from apgenericname import APGenericName
from apcomplexdiagram import APComplexDiagram
from pathlib import Path

# Create Anti-pattern objects
def createAntiPatterns():
    antiPattern = APCrossLevelTransition()
    antiPatterns.append(antiPattern)

    antiPattern = APMissingEvent()
    antiPatterns.append(antiPattern)
    
    antiPattern = APGenericName()
    antiPatterns.append(antiPattern)
    
    
    antiPattern = APComplexDiagram()
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

