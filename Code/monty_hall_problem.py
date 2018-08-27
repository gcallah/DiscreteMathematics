"""
Author: Rodrigo Arguello
"""
import random

def runSim():
    success = 0
    for i in range(100):
        prize = random.randint(1,3)
        guess = random.randint(1,3)
        doors = [1, 2, 3]
        doors.remove(guess)
        #if door has goat, get rid of that door, else get rid of other door
        if(doors[0] != prize):
            del doors[0]
        else:
            del doors[1]
        if(doors[0] == prize):
            success += 1
    return success

def runTrials(n,yesNo):
    avg = 0
    if(yesNo == "Y"):
        print("Each 100 trials averaged: ")
    #adds up n amount of success rates
    for i in range(1,n+1):
        show = runSim()
        avg += show
        #print each success rate
        if (yesNo == "Y"):
            print("(",i,")" ,show,sep='')
    #avg = average amount of success rates (total success rate percentage over # of success rates)
    avg /= n
    print("The average of all trials is:",avg)
print("We'll show through simulation that changing the selection in the Monty Hall problem leads to a 66% success rate.")
n = int(input("Input the number of 100 attempts you'd like to carry out: "))
yesNo = input("Would you like to show the average for each 100 trials? (Y/N) ")

print(runTrials(n,yesNo))
