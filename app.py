def add(numbers):
    if numbers == "":
        return 0
    else:
        delimiter = ""
        if numbers[0:2] == "//":
            numbers = numbers[2:]
            delimiter = numbers[0]
            numbers = numbers.replace(numbers[0], " ")
        for i in numbers:
            if i == ",":
                numbers = numbers.replace(i, " ")
            elif i == "\n":
                numbers = numbers.replace(i, " ")
            elif i == delimiter:
                numbers = numbers.replace(i, " ")
        numbers = numbers.split()
        sum = 0
        for i in numbers:
            sum += int(i)
        return sum
