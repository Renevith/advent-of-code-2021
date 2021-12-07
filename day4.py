from collections import defaultdict


def day4(mode):
    with open("day4.txt") as f:
        called_numbers = f.readline().split(",")
        board_count = 0
        rows = []
        cols = []
        row_score = []
        col_score = []
        for blank_line in f:
            rows.append(defaultdict(lambda: -1))
            cols.append(defaultdict(lambda: -1))
            row_score.append(defaultdict(lambda: 0))
            col_score.append(defaultdict(lambda: 0))
            for row in range(0, 5):
                split = f.readline().split()
                for col in range(0, len(split)):
                    number = split[col]
                    rows[board_count][number] = row
                    cols[board_count][number] = col
            board_count += 1
    print(board_count, "boards")
    wins = 0
    for number in called_numbers:
        print(number)
        for board_num in range(0, board_count):
            found_in_row = rows[board_num][number]
            found_in_col = cols[board_num][number]
            if found_in_row > -1:
                del rows[board_num][number]
                del cols[board_num][number]
                row_score[board_num][found_in_row] += 1
                col_score[board_num][found_in_col] += 1

                if row_score[board_num][found_in_row] == 5 or col_score[board_num][found_in_col] == 5:
                    wins += 1
                    print("board", board_num, "won")
                    if mode == "first to win" or wins == board_count:
                        board_sum = 0
                        for num in rows[board_num]:
                            if rows[board_num][num] > -1:
                                board_sum += int(num)
                        print("number:", number)
                        print("board_num:", board_num)
                        print("board rows:", rows[board_num])
                        print("board cols:", cols[board_num])
                        print("sum:", board_sum)
                        print("product:", int(number) * board_sum)
                        exit()
                    # clear the board that won so we don't count it again:
                    rows[board_num] = defaultdict(lambda: -1)
                    cols[board_num] = defaultdict(lambda: -1)
    print()


def day4a():
    day4("first to win")


def day4b():
    day4("last to win")


if __name__ == '__main__':
    day4b()
