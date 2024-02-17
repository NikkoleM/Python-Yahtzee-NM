# The function for the rolling of a turn
import random
import collections
import numpy as np

def rollDice(hand):
    # Three rolls per a turn, initializing the roll count at zero
    rollcount = 0
    # Hand is the kept dice
    # Conditions for rolling: can only roll three times, hand cannot be filled
    while (rollcount < 3):
        dicenum = 5 - len(hand)
        # Roll is the array for the roll
        roll = []
        for i in range(dicenum):
            dice = random.randint(1, 6)
            roll.append(dice)
        rollcount += 1
        print("You rolled: ", roll)
        # Ask the player which dice they want to keep
        hold = input("Would you like to keep any of your dice? (y/n) ")
        # Failsafe for idiots that will input something else
        while hold != "n" and hold != "y":
            print("Unexpected input")
            hold = input("Would you like to keep your dice? (y/n) ")
            if hold == 'y':
                break
            elif hold == 'n':
                break
        while hold == 'y':
            # Converting the roll to a numpy array
            roll = np.asarray(roll)
            kept = int(input("Which dice would you like to keep? "))
            # Calculates the maximum number of dice that can be kept
            maximum = np.count_nonzero(roll == kept)

            amount = int(input("How many dice would you like to keep? "))
            # Create the ability to be able to hold onto certain dice

            # Finding where in the array the number chosen to keep is

            if maximum == amount:
                place = np.where(roll == kept)[0]
                # print(place)
                # The array of just the kept dice
                nums = roll[place]
                # Converting it to a list so it doesn't look like [array([1,2,3,4,5])]
                l = nums.tolist()
                # print(l)
                roll = roll.tolist()
                # Subtracting the kept dice from the roll
                roll = list((collections.Counter(roll) - collections.Counter(l)).elements())
                # print(roll)
                for i in l:
                    hand.append(i)
                print('The dice you currently have are: ', hand)
                print("Your remaining dice in the roll are: ", roll)
            # Delete the kept dice from the roll array
            # Creates the condition where less of the maximum of a kind wants to be kept
            elif maximum > amount:
                roll = roll.tolist()
                l = [kept for j in range(amount)]
                # print(l)
                # Subtracting the kept dice from the roll
                roll = list((collections.Counter(roll) - collections.Counter(l)).elements())
                # print(roll)
                for i in l:
                    hand.append(i)
                print("The dice you currently have are:", hand)
                print("Your remaining dice in the roll are: ", roll)
            # Failsafe in case the player enters an invalid number of the dice to keep
            else:
                print("Please enter a valid number of dice. ")

            hold = input('Would you like to keep any dice? (y/n) ')
        # Condition to break the loop, when the hand is filled
        if len(hand) == 5:
            break
            hand.append(i)
    for i in roll:
        hand.append(i)
    print('The dice you have are:', hand)
    return hand

