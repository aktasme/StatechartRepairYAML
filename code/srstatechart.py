from sismic.io import import_from_yaml
from sismic.model import Statechart

class SRStatechart(Statechart):
    def __init__(self):
        self.name = self.statechart.name
        self.complexity = 0.0
        self.isComplex = False