def add(numbers):
    if numbers == "":
        return 0
    else:
        # getting the delimiter from string
        delimiter = ""
        if numbers[0:2] == "//":
            numbers = numbers[2:]
            delimiter = numbers[0]

        # replacing all the delimiters with space
        for i in numbers:
            if i in [",", "\n", delimiter]:
                numbers = numbers.replace(i, " ")

        numbers = numbers.split()
        sum = 0
        negative = []

        # checking for negative numbers
        for i in numbers:
            if int(i) < 0:
                negative.append(i)
        if len(negative) > 0:
            raise Exception("negative numbers not allowed " + str(",".join(negative)))
        
        # adding all the numbers
        for i in numbers:
            if int(i) <= 1000:
                sum += int(i)
        return sum
