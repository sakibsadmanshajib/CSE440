from collection import namedtuple
from enum import Enum
from Point import Point

class Board(object):

    move_connections = {
        0:[2,4], 2:[0,4], 4:[0,2,6,8], 6:[8,10], 
        8:[6,10],10:[6,8,12,14], 12:[10,14], 14:[10,12]
    }
    capture_connections = {0:[2,4,6], 2:[0,4,8], 12:[6,10,14], 14:[8,10,12]
    }
    class goat():
        alive=True
        position = 

    class player(Enum):
        T = 1
        G = 2
        def __str__(self):
            return "Goat" if self.name == "G" else "Tiger"

    class MoveType(Enum):
        P=1 #Place
        M=2 #Move
        C=3 #Capture

        def __repr__(self):
            if self.name =="P":
                return "Place"
            elif self.name =="M":
                return "Move"
            else:
                return "Capture"
        
        def __str__(self):
            return self.__repr__()

    nt = namedtuple('Move',['f','t','mt'])

    class Move(nt):
        def __repr__(self):
            return "%s-%s-%s" % (Point.get_coord(self.f),Point.get_coord(self.t),self.mt.name)

