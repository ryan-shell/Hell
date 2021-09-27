#This file will be where the game called squeel of fortune will be made

#my categories: bosses in runescape, names of cities in gielinor, food

#import random this will be needed for when the wheel is spun
import random

categories = ["Bosses in Runescape", "Cities in Gielinor", "Food"]
words = ["General Graador", "Lumbridge", "Lasagna"]
hints = ["Boss inside of the god wars dungeon", "First City after Tutorial Island", "Favourite food of Garfield"]

#create the wheel and fill it with values from 100-900$ with increments of 50$
wheel = []
for i in range(0,22):
    wheel.append(random.randrange(2,19) * 50)
wheel.append("Bankrupt")
wheel.append("Lose A Turn")

roundNum = 1

#this is the total bank and the money from each round is appended to it at the end of the round
totalBank = [0, 0, 0]
#this is the total bank for the round.
roundBank = [0, 0, 0]

#both the round numbers and the turn number will be needed to keep track of which round it is that the player
#that currently has the turn

#functions will be declared here so that they can be used inside of main
menu = """Menu Options
---------------
1)Spin Wheel
2)Guess Word"""


def generateWord():
    global blankWord
    global word
    blankWord = words[roundNum - 1]
    word = blankWord.lower()
    for i in range(0,len(blankWord)):
        if(blankWord[i].isalpha() == True):
            blankWord = blankWord.replace(blankWord[i], "_")
    blankWord = list(blankWord)

def generateFinalWord():
    global blankWord
    global word
    blankWord = words[roundNum - 1]
    word = blankWord.lower()
    for i in range(0,len(blankWord)):
        if(blankWord[i].isalpha() == True):
            blankWord = blankWord.replace(blankWord[i], "_")
    blankWord = list(blankWord)
    for i in range(0,len(word)):
        if(word[i] == "r"):
            blankWord[i] = "r"
        if(word[i] == "s"):
            blankWord[i] = "s"
        if(word[i] == "t"):
            blankWord[i] = "t"
        if(word[i] == "l"):
            blankWord[i] = "l"
        if(word[i] == "n"):
            blankWord[i] = "n"
        if(word[i] == "e"):
            blankWord[i] = "e"

def printWord():
    temp = ""
    for i in range(0,len(blankWord)):
        temp = temp + blankWord[i]
    return temp

def regularRound():
    roundOver = False
    global roundNum
    turnNum = 0

    while roundOver == False:
        print("Player number: ",turnNum % 3, " you have ",roundBank[turnNum % 3], " Dollars on this round")
        print("The category is ", categories[roundNum - 1], "\n")
        print()
        print(menu)
        choice = input("Please choose one of the above options and enter either number 1 or 2: ")

        #Spin wheel
        if (choice == "1"):
            #random index
            randNum = random.randrange(0,24)
            print("The wheel is being spun you have landed on ", wheel[randNum])

            if(wheel[randNum] == "Lose A Turn"):
                turnNum += 1

            elif wheel[randNum] == "Bankrupt":
                roundBank[turnNum % 3] = 0
                turnNum += 1

            else:
                rewardAmt = wheel[randNum]
                print("The current status of the word is", printWord())
                guess = input("Please enter a consonant that you would like to guess: ").lower()
                #check if letter is in the word
                
                #letter is in word
                if word.find(guess) != -1:
                    roundBank[turnNum % 3] += rewardAmt

                    tempC = word
                    for i in range(0,word.count(guess)):
                        index = tempC.find(guess,i)
                        tempC = tempC.replace(guess,"_",1)
                        blankWord[index] = guess
                    if(roundBank[turnNum % 3] >= 250):
                        vowelAsk = input("Would you like to buy a vowel for $250? (Y / N): ").lower()
                        if(vowelAsk == "y" and roundBank[turnNum % 3] >= 250):
                            #remove cost
                            roundBank[turnNum % 3] -= 250

                            vowel = input("Please enter a vowel: ").lower()
                            tempV = word
                            if word.find(vowel) != -1:
                                for i in range(0,word.count(vowel)):
                                    index = tempV.find(vowel)
                                    tempV = tempV.replace(vowel,"_",1)
                                    blankWord[index] = vowel
                                print(printWord())
                            else:
                                print("That vowel is not in the word")
                                turnNum += 1
                    print(printWord())

                    if printWord() == word:
                        roundOver = True
                        roundNum = roundNum + 1
                        print("You have won this round")
                #letter is not in word
                else:
                    print("Sorry that letter is not in the word.")
                    print("Your progress so far on the word is ", printWord())
                    turnNum += 1

        #whole word guess
        elif choice == "2":
            entireGuess = input("Please input your entire guess: ").lower()
            if(entireGuess == word.lower()):
                roundOver = True
                roundNum = roundNum + 1
                print("You have won this round")

        #invalid choice
        else:
            print("Please enter a valid choice")


        #print out players point number
        #print out the category
        #print out a menu with a choice of options
        # 1) Spin Wheel and guess consonant
            #1a) Buy vowel 250 only if consonant guess is correct
        # 2) Guess Word
            #need to convert all letters to lower case and then check if they are equal if they are then round is over
            #if they arent the the round is not over
roundNum = 1

def finalRound():
    global roundNum
    maxVal = max(totalBank)
    finalPlayer = totalBank.index(maxVal)
    generateFinalWord()
    print("You have ",roundBank[finalPlayer % 3], " Dollars on this round. Player number", finalPlayer)
    print("The category is ", categories[roundNum - 1], "\n")
    print("The current status of the word is: ", printWord())
    finalGuess = input("Please enter your final guess")
    if(finalGuess == word):
        print("You have won")
        roundNum += 1
    else:
        print("You have lost")
        roundNum += 1
    roundOver = False



#main
def main():
    while roundNum < 4:
        
        generateWord()
        roundBank = [0, 0, 0]
        #roundNum = 1
        if roundNum == 1:
            regularRound()
            totalBank[0] += roundBank[0]
            totalBank[1] += roundBank[1]
            totalBank[2] += roundBank[2]
        #roundNum = 2
        elif roundNum == 2:
            regularRound()
            totalBank[0] += roundBank[0]
            totalBank[1] += roundBank[1]
            totalBank[2] += roundBank[2]
        #roundNum = 3
        elif roundNum == 3:
            finalRound()

main()




#this area will be where most of the actions occurs and it will also be the location
#all function calls occur









print(categories[0])

