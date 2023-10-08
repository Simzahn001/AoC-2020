file = open("input.txt")

numbers = []

for line in file.readlines():
    currentNumber = int(line)
    if currentNumber <= 0:
        continue
    if currentNumber > 2020:
        continue
    numbers.append(currentNumber)

file.close()

SEARCHED_SUM = 2020

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        for h in range(j + 1, len(numbers)):
            x = numbers[i]
            y = numbers[j]
            z = numbers[h]
            if x + y + z == SEARCHED_SUM:
                print(f"The three numbers: {x}, {y}, {z}")
                print(f"The sum of these three is {x + y +z}")
                print(f"And the product is {x * y * z}")
                exit()

print("No numbers matching the conditions were found!")
