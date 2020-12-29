from enum import Enum

class Point(object):

    coord_to_index = {'A1':0,          'A3': 6,          'A5': 12,
                              'B2': 4,          'B4': 10, 
                      'C1':2,           'C3': 8,         'C5': 14
                      }

    index_to_coord = {0:'A1', 2:'C1', 4:'B2', 
                      6:'A4', 8:'C3', 
                     10:'B4', 12:'A5', 14: 'C5'
                      }
    class State(Enum):
        E= None #Empty
        T=1 #Tiger
        G=2 #Goat

    def __init__(self, idx, state =None):
        super(Point,self).__init__()
        self.index = idx
        self.state = self.State(state)

    def set_state(self, state):
       self.state = self.State[state]

    def get_state(self, state):
        return self.state

    def print_state(self):
        return " " if self.State.name == "E" else self.state.name

    @classmethod
    def get_index(cls,coord):
        assert(
            len(coord)==2 and coord[0] in list('ABC') and int (coord[1]) in range(1, 4)
        ), "Invalid Coordinates: %s" % str(coord)
        return cls.coord_to_index[coord]

    @classmethod
    def get_coord(cls, index):
        assert 0 <= index <14, "Invalid index: %d" % index
        return cls.index_to_coord[index]

    @property
    def coord(self):
        return Point.get_coord(self.index)

    def __str__(self):
        return self.coord
    
    def __repr__(self):
        return self.__str__()