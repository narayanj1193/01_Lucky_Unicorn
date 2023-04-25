import random

# main routine goes here

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

# Testing loop to generate 20 tokens
# for _ in range, will do something for each object within the range given.
for number in range(0, 20):
    chosen = random.choice(tokens)

    # Adjust balance according to token

    if chosen == "unicorn":
        balance += 4

    elif chosen == "horse" or chosen == "zebra":
        balance -= 0.5

    else:
        balance -= 1

    # output
    print("Token: {} , Balance: ${}".format(chosen, balance))
