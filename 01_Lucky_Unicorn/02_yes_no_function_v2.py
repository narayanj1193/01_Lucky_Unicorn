# function
def yes_no(question):
    while True:

        # Variables
        yes_variables = ["yes", "y", "yer", "yeah"]
        no_variables = ["no", "n", "nay"]
        # Ask the user if they have played before

        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response.lower() in yes_variables:
            response = "yes"
            return response

        elif response.lower() in no_variables:
            response = "no"
            return response

        elif response.lower() == "xxx":
            break

        else:
            print("Please type either yes or no ")


# Main Routine

show_instructions = yes_no("Have you played this game before? ")

print("Your response was, {}".format(show_instructions))
