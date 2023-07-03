from typing import TypeVar, Iterator

Cell = TypeVar( "Cell" )
Neighbourhood = list[ Cell ]

class Cellular:

    def __init__( self,
                  width: int,
                  neighbours: int,
                  transition: dict[ Neighbourhood, Cell ],
                  initial: tuple[ Cell ] | None = None ) -> None:
        
        self.width = width
        self.neighbours = neighbours
        self.transition = transition

        self.automaton = [ 1 for _ in range( self.width ) ] if initial is None else initial

        self._string_repr = { 0: "□", 1: "■" }

    def make_step( self ) -> None:

        new = []
        for i in range( self.width ):
            new.append( self.transition[ self._neighbourhood( i ) ] )
        self.automaton = new

    def _neighbourhood( self, i: int ) -> tuple[ Cell ]:
        
        res = [ 0 for _ in range(self.neighbours * 2 + 1) ]
        for j in range( self.neighbours + 1 ):
            res[ self.neighbours - j ] = self.automaton[ i - j ] if i - j >= 0 else 0
            res[ self.neighbours + j ] = self.automaton[ i + j ] if i + j < self.width else 0
        return tuple(res)

    def __repr__( self ) -> str:
        return " ".join( [ self._string_repr[ cell ] for cell in self.automaton ] )


## For all transition
def all_binary( array: list[ int ], i: int ) -> Iterator[ list[ int ] ]:
    
    if i == len(array):
        yield array
        return

    array[i] = 0
    yield from all_binary( array, i + 1 )

    array[i] = 1
    yield from all_binary( array, i + 1 )


nums = [ 0, 1, 0, 1, 1, 0, 1, 0 ]

tr = {
    (0, 0, 0): nums[0],
    (1, 0, 0): nums[1],
    (0, 1, 0): nums[2],
    (1, 1, 0): nums[3],
    (0, 0, 1): nums[4],
    (1, 0, 1): nums[5],
    (0, 1, 1): nums[6],
    (1, 1, 1): nums[7]
     }


aut = Cellular( 50, 1, tr )

for _ in range( 100 ):
    print( aut )
    aut.make_step()

