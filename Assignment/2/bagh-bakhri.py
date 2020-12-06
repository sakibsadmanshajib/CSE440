graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E', 'G', 'H'],
    'G': ['F', 'H'],
    'H': ['F', 'G']
}

class Handler:
    tigerPos = ''
    g1Pos = ''
    g2Pos = ''
    g3Pos = ''

    def __init__(self, tp, g1p, g2p, g3p):
        self.tigerPos = tp
        self.g1Pos = g1p
        self.g2Pos = g2p
        self.g3Pos = g3p

    def setPos(self, objct, pos):
        if objct.name is 'Tiger':
            self.tigerPos = pos
        elif objct.name is 'Goat1':
            self.g1Pos = pos
        elif objct.name is 'Goat2':
            self.g2Pos = pos
        elif  objct.name is 'Goat3':
            self.g3Pos = pos


class Goat:
    name = ''
    position = ''
    status = 'Alive'

    def __init__(self, name, pos):
        self.name = name
        self.position = pos

    def move(self, nextpos):
        possibleMoves = graph[self.position]
        if nextpos in possibleMoves:
            self.position = nextpos
            return True
        else:
            print("Not possible.")
            return False

    def getPosition(self):
        return self.position

    def hasBackup(self):
        pass
        
class Tiger:
    name = ''
    position = ''
    status = 'Free'

    def __init__(self, name, pos):
        self.name = name
        self.position = pos

    def move(self, nextpos):
        possibleMoves = graph[self.position]
        if nextpos in possibleMoves:
            self.position = nextpos
            return True
        else:
            print("Not possible.")
            return False

    def getPosition(self):
        return self.position

    def hasBackup(self):
        pass


gh1 = Goat('A')

gh1.move('D')
print(gh1.getPosition())