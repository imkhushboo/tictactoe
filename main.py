# Board
def create_board():
    Board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    return Board


def display_board(Board):
    print(Board[0] + " | " + Board[1] + " | " + Board[2])
    print(Board[3] + " | " + Board[4] + " | " + Board[5])
    print(Board[6] + " | " + Board[7] + " | " + Board[8])


def flip_value(choosen_value):
    if choosen_value == 'X':
        choosen_value = 'O'
    else:
        choosen_value = 'X'
    return choosen_value


def winner(Board):
    val = 0
    for i in range(3):
        if (Board[3 * i] == Board[3 * i + 1] and Board[3 * i + 1] == Board[3 * i + 2] and Board[3 * i] != "-"):
            val = 1
            print("Winner is ", Board[i])
            break
        elif (Board[i] == Board[i + 3] and Board[i + 3] == Board[i + 6] and Board[i] != "-"):
            val = 1
            print("Winner is ", Board[i])
            break
        elif (Board[0] == Board[4] and Board[4] == Board[8] and Board[0] != "-"):
            val = 1
            print("Winner is ", Board[0])
            break
        elif (Board[2] == Board[4] and Board[4] == Board[6] and Board[2] != "-"):
            val = 1
            print("Winner is ", Board[2])
            break
    return val


def put_value(position, choosen_value, Board):
    cond = True
    while (cond == True):
        if Board[position - 1] == '-':
            Board[position - 1] = choosen_value
            cond = False
        else:
            print("Already Occupied")
            position = handle_position(int(input("choose another position:")))
            cond = True


def tie(Board):
    val = 0
    for j in Board:
        if j != "-":
            val = val + 1
    if val == 9:
        return 1


def choose_position(choosen_value, Board):
    cond = True
    while (cond == True):
        print(choosen_value, "'s turn")
        position = int(input("choose position from 1-9:"))
        position = handle_position(position)
        put_value(position, choosen_value, Board)
        display_board(Board)
        win = winner(Board)
        if win != 0:
            cond = False
            break
        choosen_value = flip_value(choosen_value)
        tie_val = tie(Board)
        if (tie_val == 1):
            print("Oh!!! No Its a tie")
            cond = False


def handle_choosen_value(choosen_value, Board):
    while choosen_value not in ('X', 'O'):
        choosen_value = input("Please choose X or O to start the game:")
    choose_position(choosen_value, Board)


def wanna_more(playmore):
    while playmore not in ("Y", "y", "n", "N"):
        playmore = input("please choose between Y/N")
    if playmore == 'Y' or playmore == "y":
        return 1
    else:
        return 0


def handle_position(position):
    while position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        position = int(input("Please choose postion between 1-9:"))
    return position


print("~~~~~~~~lets start Tic Tac Toe~~~~~~~~")
cond = True
while (cond == True):
    Board = create_board()
    display_board(Board)
    choosen_value = input("Choose from  X or O:")
    handle_choosen_value(choosen_value, Board)
    val = wanna_more(input("Wants to play more Y/N:"))
    if val == 0:
        cond = False
    else:
        cond = True