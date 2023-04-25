# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("\n Press <Enter> to begin playing... ")
print("Your starting amount is: ${}\n".format(balance))

while play_again != "xxx":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("Balance: ${:.2f}".format(balance))
    print()

    play_again = input("Press <Enter> to play again, or 'xxx' to quit: ")
    print()

    if balance <= 0:
        play_again = "xxx"
        print("Sorry you have run out of money.")


print()
print("Total rounds played: {}".format(rounds_played))
print("Final Balance: ${}".format(balance))
