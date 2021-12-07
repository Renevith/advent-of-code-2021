from collections import defaultdict


def day3a():
    freq = defaultdict(lambda: 0)
    count = 0
    with open("day3.txt") as f:
        width = len(f.readline()) - 1
    with open("day3.txt") as f:
        for line in f:
            count += 1
            for i in range(0, width):
                freq[i] += int(line[i])
    print(count)
    for i in range(0, width):
        print(freq[i])
    gamma = 0
    epsilon = 0
    for i in range(0, width):
        gamma *= 2
        epsilon *= 2
        if freq[i] + freq[i] > count:
            gamma += 1
        elif freq[i] + freq[i] < count:
            epsilon += 1
        else:
            raise Exception("equal split")
    print("gamma: ", gamma)
    print("epsilon: ", epsilon)
    print("product: ", gamma * epsilon)


def day3b():
    freq_for_most = defaultdict(lambda: 0)
    freq_for_least = defaultdict(lambda: 0)
    count_for_most = defaultdict(lambda: 0)
    count_for_least = defaultdict(lambda: 0)
    most = []
    least = []
    with open("day3.txt") as f:
        width = len(f.readline()) - 1
    for digit in range(0, width):
        with open("day3.txt") as f:
            for line in f:
                include_for_most = True
                include_for_least = True
                for j in range(0, digit):
                    if most[j] != line[j]:
                        include_for_most = False
                    if least[j] != line[j]:
                        include_for_least = False
                if include_for_most:
                    count_for_most[digit] += 1
                    freq_for_most[digit] += int(line[digit])
                if include_for_least:
                    count_for_least[digit] += 1
                    freq_for_least[digit] += int(line[digit])
        if count_for_most[digit] == 1:
            most.append(str(freq_for_most[digit]))
        elif freq_for_most[digit] + freq_for_most[digit] >= count_for_most[digit]:
            most.append("1")
        else:
            most.append("0")
        if count_for_least[digit] == 1:
            least.append(str(freq_for_least[digit]))
        elif freq_for_least[digit] + freq_for_least[digit] >= count_for_least[digit]:
            least.append("0")
        else:
            least.append("1")
        # print("digit ", digit)
        # print("count: ", count_for_least[digit])
        # print("freq: ", freq_for_least[digit])
        # print("least: ", least)
    oxy = 0
    co2 = 0
    for i in range(0, width):
        oxy *= 2
        co2 *= 2
        if most[i] == "1":
            oxy += 1
        if least[i] == "1":
            co2 += 1
    print("oxy: ", oxy)
    print("co2: ", co2)
    print("product: ", oxy * co2)


if __name__ == '__main__':
    day3b()
