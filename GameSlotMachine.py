import random

MAX_LINES = 3 # globally declared constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# symbol_count is a dictionary
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] # column 0 at the current row
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check: # if symbols are not same, code breaks and check continues on next row 
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []                                # empty list
    for symbol, symbol_count in symbols.items():    # .items gives the key-value pair of the dictionary
        for _ in range(symbol_count):               # _ is an anonymous variable
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #slicing / making a copy of the all_symbols list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")
        
        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit(): # isdigit is a method used with strings to validate a positive whole number
            amount = int(amount) # converts the string amount into interger amount
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? $")
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Insufficient funds, your current balance is ${balance}")   
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You have won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}.")
        answer = input("Press Enter to play (and q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You are left with ${balance}.")
     
main()
