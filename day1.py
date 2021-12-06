def day1a():
    increasecount = 0
    with open("day1.txt") as f:
        prevdepth = int(f.readline())
        for line in f:
            depth = int(line)
            if depth > prevdepth:
                increasecount += 1
            prevdepth = depth
    print(increasecount)


def day1b():
    increasecount = 0
    prevdepth = []
    with open("day1.txt") as f:
        prevdepth.append(int(f.readline()))
        prevdepth.append(int(f.readline()))
        prevdepth.append(int(f.readline()))
        i = 0
        for line in f:
            depth = int(line)
            if depth > prevdepth[i]:
                increasecount += 1
            prevdepth[i] = depth
            i += 1
            if i > 2:
                i = 0
    print(increasecount)


if __name__ == '__main__':
    day1b()
