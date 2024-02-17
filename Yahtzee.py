# Nikkole Merton
# ENAE380
# Final Project

import random
import numpy as np
import collections
import roll
import scorecard

# Main game function
class main(): 

		# Game allows the game to run

		def game(self):
			play = 'y'
			while play == 'y':
				print("Welcome to Yahtzee!")

				# Ask number of players
				playeramount = int(input('How many players are there? (From 2 to 10 players) '))
				# Checking if the conditions for the proper number of players is met
				while (playeramount <= 1) or (playeramount > 10):
					print("Invalid number of players")
					playeramount = int(input('How many players are there? (From 2 to 10 players) '))
				# Creation of the scorecards
				scoreCards = {}
				# Categories of the scorecards
				categories = {'Ones' : None , 'Twos' : None , 'Threes' : None, 'Fours' : None, 'Fives' : None, 'Sixes' : None, '3 of a Kind' : None,
							  '4 of a Kind' : None, 'Full House' : None, 'Small Straight' : None, 'Large Straight' : None, 'Yahtzee' : None, 'Chance' : None}
				playerNames = []
				# Loop that allows the amount of players to enter their names
				print("Enter names of the players")
				for i in range(playeramount):
					playerNames.append(input(""))
				print(playerNames)
				# Creation of the scorecards with corresponding names
				for i in range(playeramount):
					scoreCards[str(playerNames[i])] = {'Ones': None, 'Twos': None, 'Threes': None, 'Fours': None, 'Fives': None,
													   'Sixes': None, '3 of a Kind': None, '4 of a Kind': None,
													   'Full House': None, 'Small Straight': None, 'Large Straight': None,
													   'Yahtzee': None, 'Chance': None}

				print(scoreCards)
				# Implement turn system
				# Amount of rounds in Yahtzee is 13 rounds, which fills up the scorecard
				rounds = 13
				for i in range(rounds):
					for j in range(playeramount):
						currHand = []
						# The current player
						currPlayer = playerNames[j]
						# Display whose turn it is
						print(currPlayer, " It's your turn! ")
						print('Your scorecard is: ', scoreCards[currPlayer])
						# The current player using the roll function to roll the dice
						roll.rollDice(currHand)
						print(currPlayer, " your hand is: ", currHand)
						print(currPlayer, ": ", scoreCards[currPlayer])
						# The current player selecting a value of the scorecard for the hand
						scorecard.select(scoreCards[currPlayer], currHand)
						print(currPlayer, ": ", scoreCards[currPlayer])
				# Add up the points on each player's scorecard
				totalScores = []
				for j in range(playeramount):
					# The current player
					currPlayer = playerNames[j]
					totalScore = sum(scoreCards[currPlayer].values())
					totalScores.append(totalScore)
					print(currPlayer, ': your score is', totalScore)
				# Finding the maximum score
				max = 0
				for i in range(len(totalScores)):
					if totalScores[i] > max:
						max = totalScores[i]
				# Finding the winner/s
				winners = []
				for k in range(len(totalScores)):
					if totalScores[k] == max:
						winners.append(k)

				# Displaying the winner
				# Check if there's a tie
				if len(winners) > 1:
					# Displaying the winner if there are multiple winners
					print('The winners are: ')
					for j in range(len(winners)):
						print(playerNames[winners[j]])
				else:
					# Displaying the winner when there is one winner
					print('The winner is: ', playerNames[winners[0]])

				play = input('Would you like to play again? (y/n) ')



c = main()
g = c.game()


