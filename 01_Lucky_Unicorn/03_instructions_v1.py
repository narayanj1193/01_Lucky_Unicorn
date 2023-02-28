# Functions go here...
def yes_no(question):
    while True:

        # Variables
        yes_variables = ["yes", "y", "yer", "yeah"]
        no_variables = ["no", "n", "nay", "taemin"]
        # Ask the user if they have played before

        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response.lower() in yes_variables:
            return "yes"

        elif response.lower() in no_variables:
            return "no"

        elif response.lower() == "xxx":
            break

        else:
            print("Please type either yes or no ")


def instructions():
    print("*** How to Play ***")
    print()
    print("These are the rules:")
    print()
    return ""


# Main routine

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()


print()
