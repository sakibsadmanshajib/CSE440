from enum import Enum

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

    A0 = 'A0'
    A2 = 'A2'
    A4 = 'A4'
    B1 = 'B1'
    B3 = 'B3'
    C0 = 'C0'
    C2 = 'C2'
    C4 = 'C4'

    def is_empty(self, pos):
        if self.get(pos) != 'G1' or 'G2' or 'G3' or 'T':
            return True
        else:
            return False

    def get(self, pos):
        if pos == 'A0':
            return self.A0
        elif pos == 'A2':
            return self.A2
        elif pos == 'A4':
            return self.A4
        elif pos == 'B1':
            return self.B1
        elif pos == 'B3':
            return self.B3
        elif pos == 'C0':
            return self.C0
        elif pos == 'C2':
            return self.C2
        elif pos == 'C3':
            return self.C4

    def set(self, pos, name):
        if pos == 'A0':
            self.A0 = name
        elif pos == 'A2':
            self.A2 = name
        elif pos == 'A4':
            self.A4 = name
        elif pos == 'B1':
            self.B1 = name
        elif pos == 'B3':
            self.B3 = name
        elif pos == 'C0':
            self.C0 = name
        elif pos == 'C2':
            self.C2 = name
        elif pos == 'C3':
            self.C4 = name

    def show(self):
        str = """
        {0}         {1}         {2}
        | \\\ | // | \\\ | // |
             {3}         {4} 
        | // | \\\ | // | \\\ |
        {5}         {6}         {7}
        """
        print(str.format(self.A0, self.A2, self.A4,
                         self.B1, self.B3, self.C0, self.C2, self.C4))

    # def getNeighbour(self, board, current_pos):

    #     if(current_pos=='A0' or 'A2' or 'A4' or 'B1' or 'B3' or 'C0' or 'C2' or 'C3'):
    #         return board[current_pos]

    #     else:
    #         print("Invalid Move")


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

class Animal(object):

    name = ''
    position = ''
    status = ''

    def __init__(self, pos, name, board):
        self.name = name
        self.set_position(pos, board)

    def valid_moves(self):
        possible_moves = board[self.position]
        for _ in board[self.position]:
            pass
        return board[self.position]

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def set_position(self, pos, board):
        self.position = pos
        board.set(self.position, self.name)

    def move(self, nextpos, board):
        board.set(self.position, self.position)
        self.set_position(nextpos, board)


class Goat(Animal):

    status = 'Alive'
    active = False

    # def move(self, nextpos):
    #     possibleMoves = graph[self.position]
    #     if nextpos in possibleMoves:
    #         self.position = nextpos
    #         return True
    #     else:
    #         print("Not possible.")
    #         return False

    def has_backup(self):
        pass

    def set_active(self, state):
        self.active = state

    def get_active(self):
        return self.active


class Tiger(Animal):

    status = 'Free'

    # def move(self, nextpos):
    #     possibleMoves = #graph[self.position]
    #     if nextpos in possibleMoves:
    #         self.position = nextpos
    #         return True
    #     else:
    #         print("Not possible.")
    #         return False


# class gameDashboard:
#     tiger = Tiger("Tiger","D")
#     g1 = Goat("Goat1","A")
#     g2 = Goat("Goat2","B")
#     g3 = Goat("Goat3","C")
#     h = Handler(tiger,g1,g2,g3)

class Game(object):

    bd = Board()
    bd.show()
    g1 = Goat('A0', 'G1', bd)
    g2 = Goat('B1', 'G2', bd)
    g3 = Goat('C0', 'G3', bd)
    t = Tiger('B3', 'T', bd)
    bd.show()

    # def goat_move_is_valid(self,next_move):
    #     if(g1.get_position()==next_move):
    #         return False
    #     elif (g2.get_position()==next_move):
    #         return False
    #     elif (g3.get_position() == next_move):
    #         return False
    #     elif (t.get_position()== next_move):
    #         return False
    #     else:
    #         return True

    # def goat_is_safe(self):
    #     tiger_pos=t.get_position()

    #     if(p1==g1.get_position):

    #         return True
    def get_animal(self, name):
        if name == 'G1':
            return self.g1
        elif name == 'G2':
            return self.g2
        elif name == 'G3':
            return self.g3
        elif name == 'T':
            return self.t
        else:
            return None

    def show_possible_move(self, an):
        anm = self.get_animal(an)
        count = 0

        print("Possible Moves of " + anm.get_name() + ":")
        res = anm.valid_moves()

        if self.g1.get_position() in res:
            res.remove(self.g1.get_position())
        if self.g2.get_position() in res:
            res.remove(self.g2.get_position())
        if self.g3.get_position() in res:
            res.remove(self.g3.get_position())
        if self.t.get_position() in res:
            res.remove(self.t.get_position())

        for _ in res:
            print(str(count) + ": " + _)
            count += 1

        print("Please enter a number from above: ")
        return res[int(input())]
    
    def get_board(self):
        return self.bd


def main():
    # bd = Board()
    # bd.show()
    game = Game()
    
    game.get_animal('G2').move(game.show_possible_move('G2'), game.get_board())
    game.get_board().show()


if __name__ == '__main__':
    main()
