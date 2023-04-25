import random

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
    token_number = random.randint(1, 100)

    # Adjust balance according to token
    # if the random # is between 1 and 5 (5%)
    # user gets a unicorn (adds $4 to balance)
    if 5 >= token_number >= 0:
        token = "unicorn"
        balance += 4

    # if the random # is between 6 and 36 (30%)
    # user gets a donkey (takes away $1 from balance)
    elif 36 >= token_number >= 6:
        token = "donkey"
        balance -= 1

    # if the random # is between 37 and 100 (65%)
    # user will either get a horse or zebra. If even = horse, else zebra.
    else:
        if token_number % 2 == 0:
            token = "horse"
        else:
            token = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is now ${:.2f}".format(token, balance))

    play_again = input("Press <Enter> to play again, or 'xxx' to quit: ")
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money.")


print()
print("Total rounds played: {}".format(rounds_played))
print("Final Balance: ${}".format(balance))
