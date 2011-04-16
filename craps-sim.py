import random

# declare variables to use across all games
totalwinnings = 0
totalrolls = 0
actualodds4 = 2
actualodds5 = 1.5
actualodds6 = 1.2

# declare variables which may change in GA play
startingbank = 200
bet = 10
maxbudget = 400
minbudget = 0
multipleon4 = 3
multipleon5 = 4
multipleon6 = 5


# function to roll the dice
def rollem():
	dice = random.randint(1,6) + random.randint(1,6)
	return dice

# function which plays a round - from the come out roll through crapping out or making a point
def playround():
	numberofrolls = 1
	sum = 0
	point = 0
	comeoutroll = rollem()
	if comeoutroll == 7:
		sum = bet
	elif comeoutroll == 11:
		sum = bet
	elif comeoutroll == 2:
		sum = bet * -1
	elif comeoutroll == 3:
		sum = bet * -1
	elif comeoutroll == 12:
		sum = bet * -1
	else:
		point = comeoutroll
				
		if point == 4:
			localodds = actualodds4
			localmultiple = multipleon4
		elif point == 5:
			localodds = actualodds5
			localmultiple = multipleon5
		elif point == 6:
			localodds = actualodds6
			localmultiple = multipleon6
		elif point == 8:
			localodds = actualodds6
			localmultiple = multipleon6
		elif point == 9:
			localodds = actualodds5
			localmultiple = multipleon5
		else:
			localodds = actualodds4
			localmultiple = multipleon4
			
			
		while comeoutroll != 0:
			numberofrolls += 1
			doubledice = rollem()
			if doubledice == 7:
				comeoutroll = 0
				sum = (bet * localmultiple * -1) + (bet * -1)
			elif doubledice == point:
				comeoutroll = 0
				sum = (bet * localodds * localmultiple) + (bet)
	return sum, numberofrolls
	


# function to keep playing rounds until you hit pre-determined limits	
def playaday():
	dailybankroll = startingbank
	dailyrolls = 0
	outofbudget = 0
	
	while outofbudget == 0:
		roundsum, rolls = playround()
		dailybankroll = dailybankroll + roundsum
		dailyrolls = dailyrolls + rolls		

# ends game if player reaches pre-defined maximum bankroll
		if dailybankroll >= maxbudget:
			outofbudget = 1
# ends game if player reaches pre-definied minimum bankroll
		elif dailybankroll <= minbudget:
			outofbudget = 1

	winnings = dailybankroll - startingbank
	
	return winnings, dailyrolls
	
file = open("crapsresults.csv", "a")

# play a certain number of rounds
for i in range(1,10000):
	daywinnings, dayrolls = playaday()
	totalwinnings = totalwinnings + daywinnings
	totalrolls = totalrolls + dayrolls
	file.write("%s,%s,%s,%s\n" % (totalwinnings, totalrolls, daywinnings, dayrolls))
	
file.close()

print "All in all you won: ", totalwinnings
print "It took this many rolls: ", totalrolls
print "Winnings per roll: ", (totalwinnings/totalrolls)