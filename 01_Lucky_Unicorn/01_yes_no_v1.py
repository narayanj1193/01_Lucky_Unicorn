

show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    print("")
    show_instructions = input("Have you played before? ").lower()

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("Display Instructions")

    # If they say no, output 'display instructions'
    else:
        print("Please answer yes / no")
