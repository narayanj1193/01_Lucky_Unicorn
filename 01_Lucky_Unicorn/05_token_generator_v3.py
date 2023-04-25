import random

# main routine goes here


STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 10):
    token_number = random.randint(1, 100)

    # Adjust balance according to token
    # if the random # is between 1 and 5 (5%)
    # user gets a unicorn (adds $4 to balance)
    if 5 >= token_number >= 0:
        token = "unicorn"
        balance += 4

    # if the random # is between 6 and 36 (30%)
    # user gets a donkey (takes away $1 from balance)
    elif 36 >= token_number >= 6:
        token = "donkey"
        balance -= 1

    # if the random # is between 37 and 100 (65%)
    # user will either get a horse or zebra. If even = horse, else zebra.
    else:
        if token_number % 2 == 0:
            token = "horse"
        else:
            token = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is now ${:.2f}".format(token, balance))


# output
print("\nStarting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))

