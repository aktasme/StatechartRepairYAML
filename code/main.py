from sismic.io import import_from_yaml
from sismic.io import export_to_plantuml
from sismic.model import Statechart
from srstatechart import SRStatechart
from apcomplexdiagram import APComplexDiagram

antiPatterns = []

def createAntiPatterns():
    antiPattern = APComplexDiagram()
    antiPatterns.append(antiPattern)

statechart = import_from_yaml(filepath='d:\GitHub\StatechartRepairYAML\data\simple.yaml')
assert isinstance(statechart, Statechart)

createAntiPatterns()

for antiPattern in antiPatterns:
    antiPattern.control(statechart)
    antiPattern.srprint()

# export_to_plantuml(statechart,filepath='d:\GitHub\StatechartRepairYAML\data\simple.txt')

