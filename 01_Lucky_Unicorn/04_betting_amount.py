# Functions at the top

# Main Routine
error = "Please enter a whole number that is between 1 and 10. \n"

while True:
    try:
        # Ask the question
        response = int(input("Please enter your betting amount: "))

        # if the amount is too low / too high give
        if 0 < response <= 10:
            print("You have asked to play with ${} \n".format(response))

        else:
            print(error)

    except ValueError:
        print(error)
