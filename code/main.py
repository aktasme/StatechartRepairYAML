from statechart import Statechart
from apcrossleveltransition import APCrossLevelTransition
from apmissingevent import APMissingEvent
from apgenericname import APGenericName
from apunreachablestate import APUnreachableState
from apcascadedcondition import APCascadedCondition
from apisolatedstate import APIsolatedState
from apcomplexdiagram import APComplexDiagram
from pathlib import Path

antiPatterns = []

# Create Anti-pattern objects
def createAntiPatterns():
    antiPattern = APCrossLevelTransition()
    antiPatterns.append(antiPattern)

    antiPattern = APMissingEvent()
    antiPatterns.append(antiPattern)
    
    antiPattern = APGenericName()
    antiPatterns.append(antiPattern)
    
    antiPattern = APUnreachableState()
    antiPatterns.append(antiPattern)

    antiPattern = APCascadedCondition()
    antiPatterns.append(antiPattern)

    antiPattern = APIsolatedState()
    antiPatterns.append(antiPattern)
   
    antiPattern = APComplexDiagram()
    antiPatterns.append(antiPattern)

# Start with creating patterns    
createAntiPatterns()

# Find all YAML Statechart files in data folder
for sourceFile in Path('data').rglob('*.yaml'):
    statechart = Statechart(sourceFile)

    for antiPattern in antiPatterns:
        antiPattern.control(statechart)
        #antiPattern.print()

    # Print formatted statechart results
    statechart.print()

    # Export repaired statecharts to results folder
    statechart.export()
