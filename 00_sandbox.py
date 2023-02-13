# asks users for a number
get_number = int(input("Choose a number? "))


# multiplies number by 5
times_five = get_number * 5

answer = "{} multiplied by 5 is equal to {}".format(get_number, times_five)

# output the result
print(answer)