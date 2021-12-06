def day2a():
    depth = 0
    hpos = 0
    with open("day2.txt") as f:
        for line in f:
            split = line.split(" ")
            if split[0] == "forward":
                hpos += int(split[1])
            elif split[0] == "down":
                depth += int(split[1])
            elif split[0] == "up":
                depth -= int(split[1])
                if depth < 0:
                    depth = 0

    print("depth: ", depth)
    print("hpos: ", hpos)
    print("product: ", depth * hpos)


def day2b():

    depth = 0
    hpos = 0
    aim = 0
    with open("day2.txt") as f:
        for line in f:
            split = line.split(" ")
            if split[0] == "forward":
                hpos += int(split[1])
                depth += aim * int(split[1])
                if depth < 0:
                    depth = 0
            elif split[0] == "down":
                aim += int(split[1])
            elif split[0] == "up":
                aim -= int(split[1])

    print("depth: ", depth)
    print("hpos: ", hpos)
    print("aim: ", aim)
    print("product: ", depth * hpos)


if __name__ == '__main__':
    day2b()
