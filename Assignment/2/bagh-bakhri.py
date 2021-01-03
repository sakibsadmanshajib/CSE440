from enum import Enum
import functools
import operator


class Board(object):

    A0 = 'A0'
    A2 = 'A2'
    A4 = 'A4'
    B1 = 'B1'
    B3 = 'B3'
    C0 = 'C0'
    C2 = 'C2'
    C4 = 'C4'

    gr_board = {
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

    def get_gr_board(self, pos):
        return self.gr_board[pos]

    def is_empty(self, pos):
        lst_1 = ['G1', 'G2', 'G3', 'T']
        if self.get(pos) not in lst_1:
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
        elif pos == 'C4':
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
        elif pos == 'C4':
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

class Animal(object):

    name = ''
    position = ''
    status = ''
    type = ''

    def __init__(self, pos, name, board, type):
        self.name = name
        self.set_position(pos, board)
        self.type = type

    def valid_moves(self, board):
        return board.get_gr_board(self.position)

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

    def get_type(self):
        return self.type


class Goat(Animal):

    def __init__(self, pos, name, board):
        super().__init__(pos, name, board, 'Goat')

    status = 'Alive'
    active = False

    def has_backup(self):
        pass

    def set_active(self, state):
        self.active = state

    def get_active(self):
        return self.active


class Tiger(Animal):

    def __init__(self, pos, name, board):
        super().__init__(pos, name, board, 'Tiger')

    status = 'Free'

class Game(object):

    bd = Board()
    bd.show()
    g1 = Goat('A0', 'G1', bd)
    g2 = Goat('B1', 'G2', bd)
    g3 = Goat('C0', 'G3', bd)
    t = Tiger('B3', 'T', bd)
    bd.show()

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

    def goat_is_safe(self, g):
        self_animal = self.get_animal(g)

        _safe_connections={ 'A0':['C0','A2','B1'], 'C0':['A0','B1','C2'],'B1':['A0','A2','C2','C0'],
                            'A2':['C2','A4','B3','A0'],'C2':['B3','C4','A2','C0'],'B3':['A2','C2','A4','C4'],
                            'A4':['B3','A2','C4'],'C4':['A4','B3','C2']
        }
        safe_coord=_safe_connections[self_animal.get_position()]
        print(safe_coord)
        for pos in safe_coord:
            if pos == self.g1.get_position():
                return True
            elif pos == self.g2.get_position():
                return True
            elif pos == self.g3.get_position():
                return True
        return False
        # f_depth = self.bd.get_gr_board(self_animal.get_position())
        # print(f_depth)

        # if self_animal.get_type() == 'Goat':
        #     if self.g1.get_position() in f_depth:
        #         print(self.g1.get_position())
        #         return True
        #     elif self.g2.get_position() in f_depth:
        #         print(self.g2.get_position())
        #         return True
        #     elif self.g3.get_position() in f_depth:
        #         print(self.g3.get_position())
        #         return True
        #     else:
        #         print("None")
        #         return False
        # else:
        #     print("Tiger")
        #     return False

    def kill(self):
        return False

    def minmax(self):
        # if a leaf node is reached, return the score
        # find the minimum attainable value for the minimizer
            # first make the move
            # go deeper in the search tree recursively
            # then revert the move
        # find the maximum attainable value for the maximizer
            # first make the move
            # go deeper in the search tree recursively
            # then revert the move
        pass

    def show_possible_move(self, an):
        anm = self.get_animal(an)
        count = 0

        res = anm.valid_moves(self.bd)

        if self.g1.get_position() in res:
            res.remove(self.g1.get_position())
        if self.g2.get_position() in res:
            res.remove(self.g2.get_position())
        if self.g3.get_position() in res:
            res.remove(self.g3.get_position())
        if self.t.get_position() in res:
            res.remove(self.t.get_position())
        if res:
            print("Possible Moves of " + anm.get_name() + ":")
            for _ in res:
                print(str(count) + ": " + _)
                count += 1
            q = int(input("Please enter a number from above: "))
            return res[q]
        else:
            print("No possible moves for " + anm.get_name() + ".")
            return None

    def get_board(self):
        return self.bd


def main():

    game = Game()
    print(game.get_board().get_gr_board('B1'))
    while not game.kill():
        
        print("""
Enter Animal: 
1: G1
2: G2
3: G3
4: T
            """)
        # print("Enter Number: ")
        n = int(input("Enter Number: "))
        if n == 1:
            x = 'G1'
        elif n == 2:
            x = 'G2'
        elif n == 3:
            x = 'G3'
        elif n == 4:
            x = 'T'
        # print(game.get_board().get_gr_board('B1'))
        s = game.show_possible_move(x)
        if s:
            #print(game.get_board().get_gr_board('B1'))
            game.get_animal(x).move(s, game.get_board())
            game.get_board().show()
            print(game.goat_is_safe(x))
        else:
            print(game.get_board().get_gr_board('B1'))
            pass
            

if __name__ == '__main__':
    main()
