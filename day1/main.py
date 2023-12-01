import re

DEBUG = False

number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9}

def get_number(input: str) -> int:
    if len(input) == 1:
        return int(input)
    return number[input]
    

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        line = line.strip()
        digit = r'\d|one|two|three|four|five|six|seven|eight|nine'
        single_rex = '.*?({}).*'.format(digit)
        double_rex = '.*?({}).*({}).*'.format(digit, digit)
        single_match = re.fullmatch(single_rex, line)
        double_match = re.fullmatch(double_rex, line)
        if double_match is None:
            current_number = int("{}{}".format(get_number(single_match.group(1)), get_number(single_match.group(1))))
            sum += int(current_number)
        else:
            current_number = int("{}{}".format(get_number(double_match.group(1)), get_number(double_match.group(2))))
            sum += int(current_number)
        if DEBUG:
            print("current number: {}, line: {}, sum: {}".format(current_number, line, sum))
    print ("sum: {}".format(sum))
    pass
