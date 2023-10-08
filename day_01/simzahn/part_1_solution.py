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
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == SEARCHED_SUM:
            print("The two numbers: ", str(numbers[i]), ", ", str(numbers[j]))
            print("The sum of these two is ", numbers[i] + numbers[j])
            print("And the product is ", numbers[i] * numbers[j])
            exit()

print("No numbers matching the conditions were found!")
