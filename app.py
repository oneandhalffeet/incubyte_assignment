import re
def add(numbers):
    if numbers == "":
        return 0
    else:
        # getting the delimiter from string
        delimiter = [",", "\n"]
        if numbers[0:2] == "//":
            # if multiple delimiters are added in list
            if numbers[2] == "[":
                delimiter.extend(re.findall(r'\[(.*?)\]', numbers))
            # if single delimiters is displayed
            else:
                delimiter.append(numbers[2])
            numbers = re.search(r'\n(.*)', numbers, re.DOTALL).group(1)

        # replacing all the delimiters with space
        for i in delimiter:
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
