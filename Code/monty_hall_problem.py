"""
Author: Rodrigo Arguello
"""
import random

def two_thirds():
    # at the moment this may get the right answer, but it does not
    # capture the logic of the problem.
    # that logic is:
    # choose random door
    # Monty Hall *eliminates* a non-chosen door and never one with prize
    # contestant switches doors
    # you assign the prize randomly, but during the choosing the prize should
    # never be checked against the guess.
    success = 0
    #for loop is to run 100 trials with random selection of each door
    for i in range(0, 100):
        prize = random.randint(1, 3)
        guess = random.randint(1, 3)
        temp = guess
        #if statement ensures the guess is changed to the other available option
        if(guess != prize):
            #while loop ensures the new option isn't the same as the last one,
            while(temp == guess):
                guess = random.randint(1,3)
        if(guess == prize):
            success += 1
    return success

def run_trials(n, show_work=True):
    avg = 0
    show = 0
    if show_work:
        print("Each 100 trials averaged: ")
    #for loop adds up n amount of success rates
    for i in range(1, n + 1):
        show = two_thirds()
        avg += show
        # print each success rate
        if show_work:
            print("(",i,")" , show, sep='')
    #avg = average amount of success rates (total success rate percentage over # of success rates)
    avg /= n
    print("And the average of all trials is:", avg)

def no_work(n):
    avg = 0
    # for loop adds up n amount of success rates
    for i in range(n):
        avg += two_thirds()
    #avg = average amount of success rates (total success rate percentage over # of success rates)
    avg /= n
    print("Average success rate of changing door:",avg)

print("We'll show through simulation that changing the selection in the Monty Hall problem leads to a 66% success rate.")
n = int(input("Input the number of trials of 100 you'd like to carry out: "))
yesNo = input("Would you like to show the average for each 100 trials? (Y/N) ")
run_trials(n, yesNo == "Y")
