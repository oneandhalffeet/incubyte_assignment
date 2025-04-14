def add(numbers):
    if numbers == "":
        return 0
    else:
        for i in numbers:
            if i == ",":
                numbers = numbers.replace(i, " ")
            elif i == "\n":
                numbers = numbers.replace(i, " ")
        numbers = numbers.split()
        sum = 0
        for i in numbers:
            sum += int(i)
        return sum
