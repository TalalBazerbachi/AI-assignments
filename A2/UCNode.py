class UCNode:
    def __init__(self, state, parent, cost, tileMoved):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.tileMoved = tileMoved

