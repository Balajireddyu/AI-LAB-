


board = [" "] * 9


lines = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]

def show():
    print()
    for i in range(0, 9, 3):
        print(" " + board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("---+---+---")
    print()

def winner():
    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def full():
    return " " not in board

# find a cell that completes a line for the given player
def find_winning_move(player):
    for a, b, c in lines:
        cells = [board[a], board[b], board[c]]
        if cells.count(player) == 2 and cells.count(" ") == 1:
            for pos in (a, b, c):
                if board[pos] == " ":
                    return pos
    return None

def agent_move():
    # 1. win if possible
    pos = find_winning_move("O")
    # 2. otherwise block the human
    if pos is None:
        pos = find_winning_move("X")
    # 3. otherwise take center, then corners, then sides
    if pos is None:
        for p in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
            if board[p] == " ":
                pos = p
                break
    board[pos] = "O"

def human_move():
    while True:
        try:
            pos = int(input("Your move (1-9): ")) - 1
            if 0 <= pos <= 8 and board[pos] == " ":
                board[pos] = "X"
                return
            print("Invalid or taken cell, try again.")
        except ValueError:
            print("Enter a number 1-9.")

print("You are X, Agent is O. Cells are numbered 1-9 (left to right, top to bottom).")
show()

while True:
    human_move()
    show()
    if winner() or full():
        break
    print("Agent's move:")
    agent_move()
    show()
    if winner() or full():
        break

w = winner()
if w == "X":
    print("You win!")
elif w == "O":
    print("Agent wins!")
else:
    print("It's a draw!")