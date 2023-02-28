# # Count up from one to 10...
#
# name = " "
# while name.lower() != "xxx":
#     name = input("Who are you? ")
#     print(name)
#
# print("We are done!")
#
# print()

def name_getter(question):
    while True:

        response = input(question)
        return response


# Main routine
name = name_getter("What is your name? ")
print("Your name is {}".format(name))
