from chess import util as u
from chess import globals as g

def isCheck() -> bool:
     kingPos = u.findKing(g.turn)

     if kingPos in g.attacked:
         return True

def isCheckMate(colour):
    pass
