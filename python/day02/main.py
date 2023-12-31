import re

colors = [
    "red",
    "blue",
    "green",
]

# 12 red cubes, 13 green cubes, and 14 blue cubes
allowed_red = 12
allowed_green = 13
allowed_blue = 14

color_def = r'(\d+)\s+(red|blue|green)'


def old():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    sum = 0

    for line in lines:
        tmp_matcher = re.fullmatch(r'Game\s+(\d+):\s(.+)', line.strip())
        if tmp_matcher is None:
            print("Err at full line match")
            exit(-1)
        game_no = int(tmp_matcher.group(1))
        subsets = tmp_matcher.group(2).strip().split(";")
        for subset in subsets:
            tmp_matcher = re.fullmatch(r'(?:({}),\s+)?(?:({}),\s+)?({})'.format(color_def, color_def, color_def), subset.strip())
            if tmp_matcher is None:
                print("Err at subset match")
                exit(-1)
            current_count = {"red": 0, "blue": 0, "green": 0}
            for i in range(1, 9, 3):
                if tmp_matcher.group(i) is not None:
                    current_count[tmp_matcher.group(i+2)] = int(tmp_matcher.group(i+1))
            # print("current count is {} red, {} green, {} blue".format(current_count["red"], current_count["green"], current_count["blue"]))
            # print("for line: {}".format(subset))
            if current_count["red"] > allowed_red or current_count["green"] > allowed_green or current_count["blue"] > allowed_blue:
                # thats an invalid game
                # print("invalid game")
                break
        else:
            # valid game
            # print("valid game")
            sum += game_no
    print("sum is {}".format(sum))

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    sum = 0

    for line in lines:
        tmp_matcher = re.fullmatch(r'Game\s+(\d+):\s(.+)', line.strip())
        if tmp_matcher is None:
            print("Err at full line match")
            exit(-1)
        game_no = int(tmp_matcher.group(1))
        subsets = tmp_matcher.group(2).strip().split(";")
        overall_count = {"red": 0, "blue": 0, "green": 0}
        for subset in subsets:
            tmp_matcher = re.fullmatch(r'(?:({}),\s+)?(?:({}),\s+)?({})'.format(color_def, color_def, color_def), subset.strip())
            if tmp_matcher is None:
                print("Err at subset match")
                exit(-1)
            current_count = {"red": 0, "blue": 0, "green": 0}
            for i in range(1, 9, 3):
                if tmp_matcher.group(i) is not None:
                    current_count[tmp_matcher.group(i+2)] = int(tmp_matcher.group(i+1))
            for color in colors:
                overall_count[color] = max(current_count[color], overall_count[color])
        power = 1
        for color in colors:
            power *= overall_count[color]
        sum += power
    print("sum is {}".format(sum))