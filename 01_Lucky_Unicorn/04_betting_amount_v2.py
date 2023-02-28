# Functions at the top
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

betting_amount = num_checker("How much would you like to play with? ", 0, 10)

print("You have chosen to spend ${} \n".format(betting_amount))
