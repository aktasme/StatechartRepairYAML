from sismic.model import StateMixin

class SRState(StateMixin):
    def __init__(self, name, depth):
        StateMixin.__init__(name)
        self.depth = depth