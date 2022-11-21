stringnumbers = input("give me some numbers")
numbers = stringnumbers.split()
output = []

for numbers in numbers:
    if int(numbers) % 2 != 0:
        output.append(numbers)
print(output)
        