#!/usr/bin/env python
# https://realpython.com/python-sleep/
import random, sys, time

print("Hi there! What's your name? ")
playerName = input().capitalize()
aiName = "0x0"
print(f"Nice to meet you {playerName}, I'm {aiName}.")

gameState = input("Would you like to play guess the number? [y|n] ")
if gameState.lower() == "n":
    print(f"That fine, I hope you have a nice day {playerName} !")
    sys.exit()
elif gameState.lower() == "y":
    pass

ruleState = input("Do you know how to play? [y|n] ")
while True:
    if ruleState.lower() == "y":
        break
    elif ruleState.lower() == "n":
        guessNumber = random.choice(range(1,101))
        print(f"Fine {playerName}, let me explain you how to play.")
        print("I will first choose a number between 1 and 100.")
        print(f"For example, let say I choose {guessNumber}. Of course, you don't know it.")
        print(f"Once I choose my number, {guessNumber} in this case, it's your turn to play.")
        print("You would give me a number between 1 and 100.")
        print("Based on your number I can only say whether my number is higher or lower.")
        print("We repeat the process until you find the right number!")
        ruleUnderstanding = input("Have you understand how to play? [y|n] ")
        if ruleUnderstanding.lower() == "y":
            break
        elif ruleUnderstanding.lower() == "n":
            continue

while True:
    print("Ok let's play then.")
    print("Let met guess")
    for i in range(4):
        print("hmm", "m" * i, sep='')
        time.sleep(1)
        guessNumber = random.choice(range(1,101))
    while gameState == "y":
        print("I got a number, so what your guess")
        playerGuess = input("Give me a number between 1 and 100 ")
        if not playerGuess.isdigit():
            print("Oy, that's not a number!")
            continue
        elif playerGuess.isdigit():
            playerGuess = int(playerGuess)
            if playerGuess < 1:
                print("This less than 1, remember I choose a number between 1 and 100.")
                continue
            elif playerGuess > 100:
                print("This more than 100, remember I choose a number between 1 and 100.")
                continue
            elif playerGuess >= 1 and playerGuess <= 100:
                if playerGuess < guessNumber:
                    print(f"{playerGuess} is too low.")
                    continue
                elif playerGuess > guessNumber:
                    print(f"{playerGuess} is too high.")
                    continue
                elif playerGuess == guessNumber:
                    print(f"{playerGuess} = {guessNumber}")
                    break
    gameState = input("Would you like to play again? [y|n] ")
    if gameState.lower() == "y":
        continue
    elif gameState.lower() == "n":
        print(f"Have a nice day {playerName}")
        sys.exit()
