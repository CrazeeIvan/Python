from random import randint

#initialise empty board
board = []

#add list to list to create 2-dimensional array
#["O", "O", "O", "O", "O"]
#["O", "O", "O", "O", "O"]
#["O", "O", "O", "O", "O"]
#["O", "O", "O", "O", "O"]
#["O", "O", "O", "O", "O"]
for x in range(5):
    board.append(["O"] * 5)

#draw board function
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
#select a random row using randint
def random_row(board):
    return randint(0, len(board) - 1)

#select a random column using randint
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)



#for testing/debugging
print ship_row
print ship_col

#beginning of our gameloop
for turn in range(4):
    #print the turn to the player
    print "Turn", turn + 1
    #print a message to the user asking for input and wait
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    #if the player guess correctly, reward + print the board, end the game loop
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        #draw a B to the gameboard array, to show where the enemy is
        board[ship_row][ship_col]="B"
        print_board(board)
        break
    else:
    #if the player guesses outside of the board size, advise them
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
    #if the player guesses a location they have already selected, advise them
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
    #else, they missed, advise them
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    #if the turns equals 3, the game is over and the player is a loser
        if (turn == 3):
            #draw a B to the gameboard array, to show where the enemy is
            board[ship_row][ship_col]="B"
            print "Game Over"
        print_board(board)
