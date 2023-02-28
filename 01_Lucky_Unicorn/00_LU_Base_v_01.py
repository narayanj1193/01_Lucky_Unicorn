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
    print("These are the rules:\n* stuff about rules *\n")
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


# Main routine

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

# Ask user how much they want to play with
betting_amount = num_checker("\n How much would you like to play with? ", 1, 10)

print("You have chosen to spend ${} \n".format(betting_amount))
