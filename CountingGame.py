import random

class NUMBERSGAME():
    def __init__(self):
        print("Let's start the game")

    def addition_problem(answer= 0):
        firstNumber = random.randint(1,10)
        secondNumber = random.randint(1,10)
        while answer != (firstNumber + secondNumber):
            if True:
                print (f"What is {firstNumber} + {secondNumber} ?")
                answer = int(input("enter answer: \n"))
                if answer == (firstNumber + secondNumber):
                    print ("Correct")
                else:
                    print("Try again")

    def subtraction_problem(answer= 0):
        firstNumber = random.randint(6,10)
        secondNumber = random.randint(1,5)
        while answer != (firstNumber - secondNumber):
            if True:
                print (f"What is {firstNumber} - {secondNumber} ?")
                answer = int(input("enter answer: \n"))
                if answer == (firstNumber - secondNumber):
                    print ("Correct")
                else:
                    print("Try again")

    def multiplication_problem(answer= 0):
        firstNumber = random.randint(1,10)
        secondNumber = random.randint(1,10)
        while answer != (firstNumber * secondNumber):
            if True:
                print (f"What is {firstNumber} * {secondNumber} ?")
                answer = int(input("enter answer: \n"))
                if answer == (firstNumber * secondNumber):
                    print ("Correct")
                else:
                    print("Try again")

    def division_problem(answer= 0):
        firstNumber = random.randint(20,100)
        secondNumber = random.randint(1,19)
        if (firstNumber%secondNumber)== 0:
            while answer != (firstNumber / secondNumber):
                if True:
                    print (f"What is {firstNumber} / {secondNumber} ?")
                    answer = int(input("enter answer: \n"))
                    if answer == (firstNumber / secondNumber):
                        print ("Correct")
                    else:
                        print("Try again")
        else:
            division_problem()
divisions =NUMBERSGAME.addition_problem()
