# who pays the bill?

import random
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

buy_the_meal = random.randint(0, len(names) - 1)
print(f"{names[buy_the_meal]} is going to buy the meal today!")
