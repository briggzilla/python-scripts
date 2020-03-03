# Lotto Drawings
import sys
print(sys.version)
# makes the = sign an equal length as the string for a cleaner opening of program.
z = len("Welcome to Hugh's Lotto Drawing!")
print("=" * z)
print("Welcome to Hugh's Lotto Drawing!")
print("=" * z)

drawn_nums = [5,11,9,42,3,49]  # the winning numbers
bets=[] # intialize user's bets list.

# Input user number bets
for i in range(6):
    x = int(input("Place your six winning numbers one at a time: "))
    bets.append(x)
# bets = [5,11,9,42,3,50] # test case for comparing a list of numbers to winning numbers.
print("Your numbers are: ", bets)
print("Now checking to see if you won...")

# initializers for counters and blank list to track hit numbers
hits = 0
bets_hits = []
print("The winning numbers are: ", drawn_nums)
for numbers in bets: # take list of numbers in bets
    if numbers in drawn_nums: # if a number in bets match a winning number in the drawn_nums list
        # notice i dont have to use a == statement
        # It will keep track of the number of winning hits 
        # it will also record which numbers it hit
        hits += 1
        bets_hits.append(numbers)
        if hits == 6: # this will trigger if a user hits all numbers.
            print("  Number of winning hits: ", hits)
            print("  You won the lottery!")
            print("  Winner!" * 5)
            exit()
print("  Number of winning hits: ", hits)
print("  The numbers you hit were:", bets_hits)
print("  Sorry, better luck next time.")
