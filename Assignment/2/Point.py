from enum import Enum

class Point(object):

    _coord_to_index = {
        'A1': 0, 'A2': 1, 'A3': 2,
        'B1': 3, 'B2': 4,
        'C1': 5, 'C2': 6, 'C3': 7
    }

    _index_to_coord = {
        0: 'A1', 1: 'A2', 2: 'A3',
        3: 'B1', 4: 'B2',
        5: 'C1', 6: 'C2', 7: 'C3',
    }

    class State(Enum):
        E = None
        T = 1
        G = 2
    
    def __init__(self, idx, state=None):
        super(Point, self).__init__()
        self.index = idx
        self.state = self.State(state)

    def set_state(self, state):
        self.state = self.State[state]

    def get_state(self):
        return self.state

    def print_state(self):
        return " " if self.state.name == "E" else self.state.name

    @classmethod
    def get_index(cls, coord):
        assert (
            len(coord) == 2 and coord[0] in list('ABC') and int(coord[1]) in range(1, 4)
        ), "Invalid Coordinates: %s" % str(coord)
        return cls._coord_to_index[coord]

    @classmethod
    def get_coord(cls, index):
        assert 0 <= index < 25, "Invalid index: %d" % index
        return cls._index_to_coord[index]

    @property
    def coord(self):
        return Point.get_coord(self.index)

    def __str__(self):
        return self.coord

    def __repr__(self):
        return self.__str__()