import sys
import itertools

NorthColors = ['r','r','r','o','o','g','r','r','s']
NorthSides =  ['h','t','t','t','h','t','h','h','t']
EastColors =  ['o','s','o','s','g','o','s','o','o']
EastSides =   ['h','t','t','t','t','t','h','h','t']
SouthColors = ['g','g','g','g','s','g','o','r','r']
SouthSides =  ['t','h','h','h','t','h','t','t','h']
WestColors =  ['s','o','s','r','r','s','g','s','g']
WestSides =   ['t','h','h','h','h','h','t','t','h']

class TurtlePart:
	def __init__(self):
		self.Color = "uninitialized"
		self.Side = "uninitialized"



class Card:
	def __init__(self):
		self.North = TurtlePart()
		self.East = TurtlePart()
		self.South = TurtlePart()
		self.West = TurtlePart()
		self.finalConfig = 0
	def turnCW(self,n):
		for i in range(0,n):
			oldNorth = self.North
			oldEast = self.East
			oldSouth = self.South
			oldWest = self.West
			self.North = oldWest
			self.East = oldNorth
			self.South = oldEast
			self.West = oldSouth
			self.finalConfig++


def createCards():
	nCards = 9
	AllCards = []
	for i in range (0,nCards-1):
		curCard = Card();
		curCard.North.Color = NorthColors[i]
		curCard.North.Side = NorthSides[i]
		curCard.East.Color = EastColors[i]
		curCard.East.Side = EastSides[i]
		curCard.South.Color = SouthColors[i]
		curCard.South.Side = SouthSides[i]
		curCard.West.Color = WestColors[i]
		curCard.West.Side = WestSides[i]
		curCard.finalConfig = 0
		AllCards.append(curCard)
	return AllCards

def RecTryToSolve(nPlaced, curOrder, AllCards, Puzzle):
	if(nPlaced == 9):
		for Card in Puzzle:
			print(Card.finalConfig)
		return true
	else:
		curCard = AllCards[curOrder[nPlaced]]
		nPlaced ++
		for i in range (0,3):
			turned = curCard.turnCW(i)
			Puzzle.append(turned)
			if(validSoFar(Puzzle)):
				if(RecTryToSolve(nPlaced, curOrder, AllCards, Puzzle)):
					return true
			Puzzle.pop(nPlaced)
		nPlaced --
		return false


def TryToSolve(curOrder, AllCards):
	nplaced = 0
	Puzzle = []
	return (RecTryToSolve(nPlaced, curOrder, AllCards, Puzzle))


if __name__=='__main__':
	
	n =  [0,1,2,3,4,5,6,7,8]
	for curOrder in itertools.permutations(n):
		AllCards = createCards()
		if(TryToSolve(curOrder, AllCards)):
			print curOrder
	
	