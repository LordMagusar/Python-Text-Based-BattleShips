from os import system 
import random

lets = "ABCDEFGHIJ"
shipFormat = [5,4,3,3,2]

P1grid = [["." for x in range(10)] for y in range(10)]
P2grid = [["." for x in range(10)] for y in range(10)] 
P2gridVisible = [["." for x in range(10)] for y in range(10)] 



P1ships = {
	"Carrier":[],#5
	"Battleship":[],#4
	"Cruiser":[],#3
	"Submarine":[],#3
	"Destroyer":[],#2
}
P2ships = {
	"Carrier":[],#5
	"Battleship":[],#4
	"Cruiser":[],#3
	"Submarine":[],#3
	"Destroyer":[],#2
}




def cpuShipPlacement():#Function used to generate CPU's ships randomly, without conflicts
	for x in enumerate(P2ships):
		letNum = random.randint(1,2)#Picks a direction for the ship to orientate. 1 = Let, 2 = Num
		if letNum == 1:
			while True:
				coords = []
				let = random.choice(lets)
				num = random.randint(0,9-shipFormat[x[0]])
				for y in range(shipFormat[x[0]]):
					coords.append(let+str(num + y))
				if coordChecker(P2ships, coords):
					continue
				break
			for coord in coords:
				P2ships[x[1]].append([coord, False, False])

		if letNum == 2:
			while True:
				coords = []
				num = random.randint(0,9)
				let = random.randint(0,9-shipFormat[x[0]])
				for y in range(shipFormat[x[0]]):
					coords.append((lets[let+y])+str(num))
				if coordChecker(P2ships, coords):
					continue
				break
			for coord in coords:
				
				P2ships[x[1]].append([coord, False, False])
	updateGrid(P2grid, P2ships)
	drawGrid(P2grid)

def playerShipPlacement():#function used to use player input to place ships
	drawGrid(P1grid)
	print("No Spaces. Capital Letters")

	for x in enumerate(P1ships):
		prevInp = None
		for y in range(shipFormat[x[0]]):
			while True:
				inp = input(f"Input co ord {y+1} for {x[1]} ({shipFormat[x[0]]} long)")

				if not(prevInp):
					prevInp = inp
					break
				if int(inp[1]) != int(prevInp[1]) and lets.index(inp[0]) != lets.index(prevInp[0]):
					print("Invalid co ordinate")
					continue
				if int(inp[1]) > 9 or int(inp[1]) < 0 or lets.index(inp[0]) > 9 or lets.index(inp[0]) < 0:
					print("Invalid co ordinate")
					continue
					
				break
			P1ships[x[1]].append([inp, False, False])
			system("cls")
			updateGrid(P1grid, P1ships)
			drawGrid(P1grid)

def updateGrid(grid, ships, visible = True): #Updates the grid to reflect events in game
	for ship in ships:
		for coords in ships[ship]:
			grid[int(coords[0][1])][lets.index(coords[0][0])] = (str(list(ships).index(ship)+1) if visible else ".") if not(coords[1]) else "x" if False in [living[1] for living in ships[ship]] else "X" #Marks ship segments with their index if they are present, x if they have been hit, X if they have been sunk
			
def drawGrid(grid):#Function used to unpack and print each line of the grid, with axis labels
	for xIndex, xGrid in enumerate(grid):
		print(xIndex, end = " ")
		for y in xGrid:
			print(y, end = " ")
		print()
	print(" ", end = " ")
	for let in lets:
		print(let, end = " ")
	print()

def coordChecker(ships, coords):#checks a given list of coordinates in comparison to a players active ships. Returns True if one or more of the given coordinates is a conflict
	flagged = False
	for shipType in ships:
		for coord in ships[shipType]:
			if coord[0] in coords:
				flagged = True
				break
		if flagged:
			break
	return flagged

def playerAttack():
	drawGrid(P2gridVisible)
	print("Player's turn")
	target = input("Enter a coordinate to strike")
	system("cls")
	found = False
	for shipType in P2ships:
		for coord in enumerate(P2ships[shipType]):
			if target == coord[1][0]:			
				coord[1][1] = True
				found = True
				print("Hit!")
				if not(False in [living[1] for living in P2ships[shipType]]):
					print("Sunk")			
				updateGrid(P2gridVisible, P2ships, False)			
				updateGrid(P2grid, P2ships)
				break
		if found:
			break
	if not found:
		print("Miss")
		try:
			P2gridVisible[int(target[1])][lets.index(target[0])] = "N"
		except exception as e:
			input(e)
	drawGrid(P2gridVisible)

def cpuAttack(guesses):
	
	if not guesses:
		target = random.choice(lets)+str(random.randint(0,9))
	else: 
		target = guesses.pop(random.randint(0, len(guesses)-1))
		

	found = False
	print(f"Target = {target}")
	
	input("CPU Turn \nEnter to continue...")
	system("cls")
	
	for shipType in P1ships:
		for coord in enumerate(P1ships[shipType]):
			if target == coord[1][0]:
				coord[1][1] = True
				found = True
				print("CPU Hit!")
				
				if not(False in [living[1] for living in P2ships[shipType]]):
					print("Sunk")	
					guesses = []
				else:
					try:
						guesses.append(target[0] + str(int(target[1]) + 1)) if int(target[1]) + 1 <=9 else None
					except IndexError: 
						pass
					try:
						guesses.append(target[0] + str(int(target[1]) - 1)) if int(target[1]) - 1 >=0 else None
					except IndexError: 
						pass
					try:
						guesses.append(lets[lets.index(target[0])+1] + target[1])
					except IndexError: 
						pass
					try:
						guesses.append(lets[lets.index(target[0])-1] + target[1])
					except IndexError: 
						pass
					
					
				updateGrid(P1grid, P1ships)
				break
		if found:
			break
	if not found:
		print("CPU miss!")
		
		P1grid[int(target[1])][lets.index(target[0])] = "N"
	updateGrid(P1grid, P1ships)
	drawGrid(P1grid)
	return guesses


cpuShipPlacement()



playerShipPlacement()


def game():
	guesses = []
	while True:
		playerAttack()
		guesses = cpuAttack(guesses)
		
				

game()
