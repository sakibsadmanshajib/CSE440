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
    A0 = 'X'
    A2 = 'X'
    A4 = 'X'
    B1 = 'X'
    B3 = 'X'
    C0 = 'X'
    C2 = 'X'
    C4 = 'X'

    def __init__(self):
        self.A0 = 'G'
        self.B1 = 'G'
        self.B3 = 'T'
        self.C0 = 'G'

    def get_A0(self):
        return self.A0

    def get_A2(self):
        return self.A2
    
    def get_A4(self):
        return self.A4

    def get_B1(self):
        return self.B1

    def get_B3(self):
        return self.B3

    def get_C0(self):
        return self.C0

    def get_C2(self):
        return self.C2

    def get_C4(self):
        return self.C4

    def set_A0(self,p):
        self.A0=p

    def set_A2(self,p):
        self.A2=p

    def set_A4(self,p):
        self.A4=p
    
    def set_B1(self,p):
        self.B1=p
    
    def set_B3(self,p):
        self.B3=p

    def set_C0(self,p):
        self.C0=p

    def set_C2(self,p):
        self.C2=p
    
    def set_C4(self,p):
        self.C4=p

    def show(self):
        str = """
        {0}         {1}         {2}
        | \\\ | // | \\\ | // |
             {3}         {4} 
        | // | \\\ | // | \\\ |
        {5}         {6}         {7}
        """
        print(str.format(self.A0, self.A2, self.A4, self.B1, self.B3, self.C0, self.C2, self.C4))

    def getNeighbour(self, board,current_pos):
        if(current_pos=='A0' or 'A2' or 'A4' or 'B1' or 'B3' or 'C0' or 'C2' or 'C3'):
            return board[current_pos]
        
        else:
            print("Invalid Move")


        



# class Handler:
#     tigerPos = ''
#     g1Pos = ''
#     g2Pos = ''
#     g3Pos = ''


#     def __init__(self, t, g1, g2, g3):
#         self.tigerPos = t.getPosition()
#         self.g1Pos = g1.getPosition()
#         self.g2Pos = g2.getPosition()
#         self.g3Pos = g3.getPosition()

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
    #name = ''
    position = ''
    status = 'Alive'
    active = False

    def __init__(self, pos):
        self.position = pos


    # def move(self, nextpos):
    #     possibleMoves = graph[self.position]
    #     if nextpos in possibleMoves:
    #         self.position = nextpos
    #         return True
    #     else:
    #         print("Not possible.")
    #         return False

    def getPosition(self):
        return self.position

    def hasBackup(self):
        pass

    def setPosition(self,pos):
        self.position=pos
    
    def setActive(self,state):
        if(state==0):
            active = False
        else:
            active=True
    
    def get_active():
        return active
        
class Tiger:

    position = ''
    status = 'Free'

    def __init__(self, pos):
        #self.name = name
        self.position = pos

    def move(self, nextpos):
        possibleMoves = #graph[self.position]
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

    

# class gameDashboard:
#     tiger = Tiger("Tiger","D")
#     g1 = Goat("Goat1","A")
#     g2 = Goat("Goat2","B")
#     g3 = Goat("Goat3","C")
#     h = Handler(tiger,g1,g2,g3)
   
class Game(object,Goat,Tiger):

    g1 = Goat('A0') 
    g2 = Goat('B3')
    g3 = Goat('A4')
    t = Tiger('B1')
    bd=Board()
    def __init__(self):
     pass 

    def goat_move_is_valid(self,next_move):
        if(g1.getPosition()==next_move):
            return False
        elif (g2.getPosition()==next_move):
            return False
        elif (g3.getPosition() == next_move):
            return False
        elif (t.getPosition()== next_move):
            return False
        else:
            return True
    
    def goat_is_safe(self):
        tiger_pos=t.getPosition()

        if(p1==g1.getPosition):
            
            return True

bd = Board()
bd.show()

