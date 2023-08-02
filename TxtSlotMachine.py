import random as rand




ROW = 3
COLS = 3

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

symbol_count = {'A':2, 
                'B':4,
                'C':6,
                'D':8}

symbol_value = {'A':5,
                'B':4, 
                'C':3, 
                'D':2}



def checkwin(c, l, b, v):
    winnings = 0
    winline = []
    for line in range(l):
        sym = c[0][line]
        for column in c:
            s2c = column[line]
            if sym != s2c:
                break
            else:
                winnings += v[sym] * b
                winline.append(line + 1)
    return winnings, winline

    


def get_slot(r, c, s):
    all_sym = []
    for symbol, symbol_count in s.items():
        for _ in range(symbol_count):
            all_sym.append(symbol)

    
    columns = []
    for _ in range(c):
        column = []
        currentsyms = all_sym[:]
        for _ in range(r):
            value = rand.choice(currentsyms)
            currentsyms.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns


def printslot(columns):
    for r in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[r], end=' | ')
            else:
                print(column[r], end='')
        print()


def deposit():
    while True:
        amount = input (' How much do you want to add? $')
        if amount.isdigit ():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Deposit must be greter than 0')
        else:
            print('Please enter a numerical amount')

    return amount


def line():
    while True:
        lines = input (' How many line do you want to bet on? (1-' + str(MAX_LINES) + ')')
        if lines.isdigit ():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a number between 1 & ' + str(MAX_LINES))
        else:
            print('Please enter a numerical amount')

    return lines

def parlay():

    while True:
        amount = input (' How much do you want to wager per line? $')
        if amount.isdigit ():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print('wager must be between $' + str(MIN_BET) + ' $' + str(MAX_BET))  #fstring wouldve been easier
        else:
            print('Please enter a numerical amount')

    return amount



def game(bal):
    lines = line()
    while True:
        bet = parlay()
        tb = bet * lines
        if tb > bal:
            print(f'Insufficient funds, current balance is ${bal}')
        else:
            break

    print(f'you are beting ${bet} on {lines} lines. The total bet equals ${tb}')

    slots = get_slot(ROW, COLS, symbol_count)
    printslot(slots)
    winnings, winline = checkwin(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    print(f'You won on', *winline)
    return (winnings - tb)



def main():

    bal = deposit()
    while True:
        print(f'current balence is ${bal}')
        spin = input("Press enter to play, or q to quit")
        if spin == 'q':
            break
        bal += game(bal)

    print(f'You made ${bal} today, thank you come again!')

    



main()