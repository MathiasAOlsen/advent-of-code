floor = 0

with open('2015\Day1\input.txt') as f:
    characters = f.read()

# characters = "(())"

for character in characters:
    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1
    else:
        print("hvad fanden, er der andre tegn?")
        print(character)

print("solution: ", floor)
