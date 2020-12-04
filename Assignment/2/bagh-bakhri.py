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

class Goat:
    position = ''
    status = 'Alive'

    def __init__(self, pos):
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
    position = ''

    def __init__(self, pos):
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