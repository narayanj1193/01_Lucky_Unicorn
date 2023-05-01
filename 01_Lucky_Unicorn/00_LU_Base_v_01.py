import random


# Functions go here...
# checks users enter yes or no
def yes_no(question):
    while True:

        # Variables
        yes_variables = ["yes", "y", "yer", "yeah"]
        no_variables = ["no", "n", "nay", "nope"]
        # Ask the user if they have played before

        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response.lower() in yes_variables:
            response = "yes"
            return response

        elif response.lower() in no_variables:
            response = "no"
            return response

        else:
            print("Please type either yes or no \n")


# Displays instructions
def instructions():
    print("\n *** How to Play *** \n")
    print("These are the rules:\n\nChoose a starting amount (minimum $1, maximum $10) \n "
          "\nYou will get either a horse, a zebra, a donkey or a unicorn.\n"
          "It costs a $1 per round. Depending on your prize you might win some of the money back."
          " Here's the payout amounts...\nUnicorn: $5.00 (balance increases by $4)\n"
          "Horse: $0.50 (balance decreases by $0.50)\n"
          "Zebra: $0.50 (balance decreases by $0.50)\n"
          "Donkey: $0.00 (balance decreases by $1)\n"
          "\nCan you avoid the donkeys, get the unicorns and walk home with the money??")
    return ""


# checks user enters an integer between a high and low number
def num_checker(question, low, high):
    # Main Routine
    error = "Please enter a whole number that is from {} to {}.".format(low, high)

    while True:
        try:
            # Ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low <= response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# creates a decorative statement to add aesthetics to the program
def statement_generator(statement, decoration, above_below):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = above_below * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine
statement_generator("Welcome to Lucky Unicorn!", "!", "*")
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

# Ask user how much they want to play with
betting_amount = num_checker("\nHow much would you like to play with? ", 1, 10)

balance = betting_amount

rounds_played = 0

play_again = input("\n Press <Enter> to begin playing... ")
statement_generator("Your starting amount is: ${}".format(balance), "*", "=")
print("")

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
        prize_decoration = "U"
        balance += 4

    # if the random # is between 6 and 36 (30%)
    # user gets a donkey (takes away $1 from balance)
    elif 36 >= token_number >= 6:
        token = "donkey"
        prize_decoration = "D"
        balance -= 1

    # if the random # is between 37 and 100 (65%)
    # user will either get a horse or zebra. If even = horse, else zebra.
    else:
        if token_number % 2 == 0:
            token = "horse"
            prize_decoration = "H"

        else:
            token = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is now ${:.2f}".format(token, balance)
    statement_generator(outcome, prize_decoration, "-")
    play_again = input("Press <Enter> to play again, or 'xxx' to quit: ")
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money.")

print()
print("Total rounds played: {}".format(rounds_played))
print(f"Final Balance ${balance:.2f}")
