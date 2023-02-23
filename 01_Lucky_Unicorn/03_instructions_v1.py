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
            print("Please answer yes / no")


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
