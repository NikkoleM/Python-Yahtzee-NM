import collections
# Function that allows the player to select where the hand goes to on the scorecard
def select(scoreCard, hand):
    a = intro(scoreCard)
    # Case switches for what category is chosen by the player
    match a:
        # When Ones is picked
        case 1:
            score = calcOnes(hand)
            print(score)
            assign(score, scoreCard, 'Ones', hand)
        # When Twos is picked
        case 2:
            score = calcTwos(hand)
            print(score)
            assign(score, scoreCard, 'Twos', hand)
        # When Threes is picked
        case 3:
            score = calcThrees(hand)
            print(score)
            assign(score, scoreCard, 'Threes', hand)
        # When Fours is picked
        case 4:
            score = calcFours(hand)
            print(score)
            assign(score, scoreCard, 'Fours', hand)
        # When Fives is picked
        case 5:
            score = calcFives(hand)
            print(score)
            assign(score, scoreCard, 'Fives', hand)
        # When Sixes is picked
        case 6:
            score = calcSixes(hand)
            print(score)
            assign(score, scoreCard, 'Sixes', hand)
        # When 3 of a Kind is picked
        case 7:
            score = calc3ofaKind(hand)
            print(score)
            assign(score, scoreCard, '3 of a Kind', hand)
        # When 4 of a Kind is picked
        case 8:
            score = calc4ofaKind(hand)
            print(score)
            assign(score, scoreCard, '4 of a Kind', hand)
        # When Full House is picked
        case 9:
            score = calcFullHouse(hand)
            print(score)
            assign(score, scoreCard, 'Full House', hand)
        # When Small Straight is picked
        case 10:
            score = calcSmallStraight(hand)
            print(score)
            assign(score, scoreCard, 'Small Straight', hand)
        # When Large Straight is picked
        case 11:
            score = calcLargeStraight(hand)
            print(score)
            assign(score, scoreCard, 'Large Straight', hand)
        # When Yahtzee is picked
        case 12:
            score = calcYahtzee(hand)
            print(score)
            assign(score, scoreCard, 'Yahtzee', hand)
        # When Chance is picked
        case 13:
            score = calcChance(hand)
            print(score)
            assign(score, scoreCard, 'Chance', hand)
        # Default case
        case default:
            print('Invalid option, please choose a valid option. ')
            select(scoreCard, hand)

# Calculating the points from the hand
# Functions based upon which option was taken

def calcOnes(hand):
    print('You picked Ones!')
    points = 0
    for i in range(len(hand)):
        if hand[i] == 1:
            points += 1
    return points

def calcTwos(hand):
    print('You picked Twos! ')
    points = 0
    for i in range(len(hand)):
        if hand[i] == 2:
            points += 2
    return points

def calcThrees(hand):
    print('You picked Threes! ')
    points = 0
    for i in range(len(hand)):
        if hand[i] == 3:
            points += 3
    return points

def calcFours(hand):
    print('You picked Fours! ')
    points = 0
    for i in range(len(hand)):
        if hand[i] == 4:
            points += 4
    return points

def calcFives(hand):
    print('You picked Fives! ')
    points = 0
    for i in range(len(hand)):
        if hand[i] == 5:
            points += 5
    return points

def calcSixes(hand):
    print('You picked Sixes! ')
    points = 0
    for i in range(len(hand)):
        if hand[i] == 6:
            points += 6
    return points

def calc3ofaKind(hand):
    print('You picked 3 of a Kind! ')
    # Creates a dictionary of the amount of times an element was repeated in an array
    count = collections.Counter(hand)
    # Gets the maximum value of the number which was repeated
    max_val = max(count.values())
    # Checking if the condition of 3 of a Kind is met
    if max_val >= 3:
        points = sum(hand)
    else:
        points = 0
    return points


def calc4ofaKind(hand):
    print('You picked 4 of a Kind! ')
    # Creates a dictionary of the amount of times an element was repeated in an array
    count = collections.Counter(hand)
    # Gets the maximum value of the number which was repeated
    max_val = max(count.values())
    # Checking if the condition of 4 of a Kind is met
    if max_val >= 4:
        points = sum(hand)
    else:
        points = 0
    return points

def calcFullHouse(hand):
    print('You picked Full House!')
    count = collections.Counter(hand)
    # Getting the maximum repeated value
    max_val = max(count.values())
    # Getting the minimum repeated value
    min_val = min(count.values())
    # Checking if the conditions for a Full House are met.
    if max_val == 3 and min_val == 2:
        # Full House is always worth 25 points
        points = 25
    else:
        points = 0
    return points

def calcSmallStraight(hand):
    print('You picked Small Straight! ')
    # Checking if the condition for a Small Straight is met.
    # Creates a dictionary of the amount of times an element was repeated in an array
    count = collections.Counter(hand)
    # Checking if the condition for a Small Straight is met
    if (count[1] >= 1 and count[2] >= 1 and count[3] >= 1 and count[4] >= 1) or (
            count[2] >= 1 and count[3] >= 1 and count[4] >= 1 and count[5] >= 1) or (
            count[3] >= 1 and count[4] >= 1 and count[5] >= 1 and count[6] >= 1):
        # Small Straight is always worth 30 points
        points = 30
    else:
        points = 0
    return points

def calcLargeStraight(hand):
    print('You picked Large Straight! ')
    # Creates a dictionary of the amount of times an element was repeated in an array
    count = collections.Counter(hand)
    # Checking if the condition for a Large Straight is met
    if (count[1] == 1 and count[2] == 1 and count[3] == 1 and count[4] == 1 and count[5] == 1) or (
            count[6] == 1 and count[2] == 1 and count[3] == 1 and count[4] == 1 and count[5] == 1):
        # Large Straight is always worth 40 points
        points = 40
    else:
        points = 0
    return points

def calcYahtzee(hand):
    print('You picked Yahtzee! ')
    # Creates a dictionary of the amount of times an element was repeated in an array
    count = collections.Counter(hand)
    # Gets the maximum value of the number which was repeated
    max_val = max(count.values())
    # Checking if the condition for Yahtzee is met
    if max_val == 5:
        # Yahtzee is always worth 50 points
        points = 50
    else:
        points = 0
    return points

def calcChance(hand):
    print('You picked Chance! ')
    # Sums up all the dice which is the score
    points = sum(hand)
    return points

# Function that assigns the value in the scorecard to the score
def assign(score, scoreCard, placement, hand):
    # Initializing valid
    valid = False
    while valid != True:
        valid = checkValidity(scoreCard, placement)
        # print("assign", valid)
        if valid == True:
            # Assigning the score to the scorecard
            scoreCard[placement] = score
        break



# Checks if category has already been filled
def checkValidity(scoreCard, placement):
    if scoreCard[placement] != None:
        # Updating the validity
        valid = False
        print('That category has been filled. Please choose another category. ')
        select(scoreCard, hand)
    else:
        valid = True
        # print('Check validity', valid)
    return valid

def intro(scoreCard):
    # Starting at Option 1
    y = 1
    print('===== Points Options =====')
    # Showing the player the options that can be made to where the points of the roll will go to
    for i in scoreCard:
        print('Option ', y, ': ', i)
        y += 1
    # Asking the player which option to pick
    argument = int(input('Which category would you like to assign your hand to? '))
    return argument







