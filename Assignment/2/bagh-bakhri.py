board = {
    'A0': ['B1', 'C0'],
    'A1': None,
    'A2': ['B1', 'C2', 'B3'],
    'A3': None,
    'A4': ['B3', 'C4'],
    'B0': None,
    'B1': ['A0', 'A2', 'C0', 'C2'],
    'B2': None,
    'B3': ['A2', 'C2', 'C4', 'A4'],
    'B4': None,
    'C0': ['A0', 'B1'],
    'C1': None,
    'C2': ['B1', 'A2', 'B3'],
    'C3': None,
    'C4': ['B3', 'A4']
}

class Board(object):
    pass

class Handler:
    tigerPos = ''
    g1Pos = ''
    g2Pos = ''
    g3Pos = ''

    def __init__(self, t, g1, g2, g3):
        self.tigerPos = t.getPosition()
        self.g1Pos = g1.getPosition()
        self.g2Pos = g2.getPosition()
        self.g3Pos = g3.getPosition()

    # def setPos(self, objct, pos):
    #     if objct.name is 'Tiger':
    #          objct.setPosition (self.tigerPos)
    #     elif objct.name is 'Goat1':
    #         objct.setPosition(self.g1Pos) 
    #     elif objct.name is 'Goat2':
    #         objct.setPosition(self.g2Pos)
    #     elif  objct.name is 'Goat3':
    #         objct.setPosition(self.g3Pos)
    

        


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

    def setPosition(self,pos):
        self.position=pos

        
        
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
    
    def setPosition(self,pos):
        self.position = pos


class gameDashboard:
    board = graph
    tiger= Tiger("Tiger","D")
    g1 = Goat("Goat1","A")
    g2 = Goat("Goat2","B")
    g3 = Goat("Goat3","C")
    h = Handler(tiger,g1,g2,g3)
   

    


