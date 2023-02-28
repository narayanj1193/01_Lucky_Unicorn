
show_instructions = ""

yes_variables = ["yes", "y", "yer", "yeah"]
no_variables = ["no", "n", "nay"]
while True:
    # Ask the user if they have played before
    print("")
    show_instructions = input("Have you played before? ").lower()

    # If they say yes, output 'program continues'
    if show_instructions.lower() in yes_variables:
        print("Program continues")

    elif show_instructions.lower() in no_variables:
        print("Display instructions")

    elif show_instructions.lower() == "xxx":
        print("*** Thanks for playing! ***")
        break
    else:
        print("Please type either yes or no ")
