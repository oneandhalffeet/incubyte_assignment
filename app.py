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
            if i in [",", "\n", delimiter]:
                numbers = numbers.replace(i, " ")
        numbers = numbers.split()
        sum = 0
        negative = []
        for i in numbers:
            if int(i) < 0:
                negative.append(i)
        if len(negative) > 0:
            raise Exception("negative numbers not allowed " + str(",".join(negative)))
        for i in numbers:
            sum += int(i)
        return sum
