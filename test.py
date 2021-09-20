
# import math

# x = 50

# print(x)

# x -= 7

# print(x)

# print(round(7/2))

# print(x + round(7/2))

x = [1, 2, 3, 4, 5, 6, 7]

print("type in a number")

raw_input = input()

if isinstance(int(raw_input), int):
    print(x[int(raw_input)])
else:
    print("invalid input")



