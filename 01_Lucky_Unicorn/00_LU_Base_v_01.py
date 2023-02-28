# Functions go here...
def yes_no(question):
    valid = False
    while not valid:

        # Ask the user if they have played before
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        # If they say no, output 'display instructions'
        else:
            print("Please answer yes / no \n")


def instructions():
    print("\n *** How to Play *** \n")
    print("These are the rules:\n* stuff about rules *\n")
    return ""


def num_checker(question, low, high):
    # Main Routine
    error = "Please enter a whole number that is between 1 and 10. \n"

    while True:
        try:
            # Ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# Main routine

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

# Ask user how much they want to play with
betting_amount = num_checker("How much would you like to play with? ", 0, 10)

print("You have chosen to spend ${} \n".format(betting_amount))
