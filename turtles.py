import sys

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

def createCards:
	nCards = 9
	AllCards = []
	for i in range nCards:
		curCard = Card();
		curCard.North.Color = NorthColors[i]
		curCard.North.Side = NorthSides[i]
		curCard.East.Color = EastColors[i]
		curCard.East.Side = EastSides[i]
		curCard.South.Color = SouthColors[i]
		curCard.South.Side = SouthSides[i]
		curCard.West.Color = WestColors[i]
		curCard.West.Side = WestSides[i]

if __name__=='__main__':
	AllCards = createCards()
	