from sismic.io import import_from_yaml
from sismic.io import export_to_plantuml
from sismic.model import Statechart

statechart = import_from_yaml(filepath='d:\GitHub\StatechartRepairYAML\data\simple.yaml')
assert isinstance(statechart, Statechart)

export_to_plantuml(statechart,filepath='d:\GitHub\StatechartRepairYAML\data\simple.txt')

