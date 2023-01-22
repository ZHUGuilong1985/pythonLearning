import random

MAX_MONEY = 1000
MIN_MONEY = 1

# 老虎机行数
MAX_LINE = 3

# 下注金额限制
MIN_BET = 10
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value= {"A": 8, "B": 6, "C": 4, "D": 2}


def get_slot_machine_spin(rows, cols, symbols):
    '''老虎机转起来'''

    # 导入列

    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_synbols = all_symbols[:]  # 切片
        for row in range(rows):
            value = random.choice(current_synbols)
            current_synbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_spot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def check_winnings(columns,lines,bet,values):


def input_money():
    '''存钱    '''

    while True:
        n = input("how much do you want in: ")
        if n.isdigit():  # 数字
            n = int(n)
            if 0 < n < 10000:  # 大小合适
                break
            else:  # 溢出
                print(f"the money must between {MIN_MONEY} and {MAX_MONEY}")
        else:  # 非数字
            print("input a number")

    return n


def get_line():
    '''选行'''
    while True:
        n = input("how line do you choose: ")
        if n.isdigit():  # 数字
            n = int(n)
            if 1 <= n <= MAX_LINE:  # 大小合适
                break
            else:  # 溢出
                print(f"the money must between 1 and {MAX_LINE}")
        else:  # 非数字
            print("input a number")

    return n


def get_bet():
    '''下注'''
    while True:
        n = input("how much do you bet: ")
        if n.isdigit():  # 数字
            n = int(n)
            if MIN_BET <= n <= MAX_BET:  # 大小合适
                break
            else:  # 溢出
                print(f"the money must between {MIN_BET} and {MAX_BET}")
        else:  # 非数字
            print("input a number")

    return n


def main():
    deposit = input_money()
    print(f"you putin {deposit} RMB, good luck! ")

    line = get_line()  # 行
    print(f"you choose line {line}. ")

    while True:
        bet = get_bet()  # 下注
        total = line * bet

        if total > deposit:
            print(f"You donot have enough money. {deposit}")

        else:
            break

    print(f"你在第{line}行下注{bet}钱，奖金共计{total}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_spot_machine(slots)


main()
