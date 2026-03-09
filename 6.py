def tic_tac_toe():
    board = [' ']*9

    def show():
        for i in [0,3,6]:
            print(board[i], '|', board[i+1], '|', board[i+2])
            if i < 6: print('--+---+--')

    def win(p):
        combos = [[0,1,2],[3,4,5],[6,7,8],
                  [0,3,6],[1,4,7],[2,5,8],
                  [0,4,8],[2,4,6]]
        return any(all(board[i]==p for i in c) for c in combos)

    turn = 0
    while turn < 9:
        show()
        p = 'X' if turn%2==0 else 'O'

        try:
            move = int(input(f"{p}'s turn (0-8): "))
            if move < 0 or move > 8:
                print("Invalid position! Try again.")
                continue
            if board[move] != ' ':
                print("Position already taken! Try again.")
                continue
        except:
            print("Enter a valid number!")
            continue

        board[move] = p

        if win(p):
            show()
            print(f"{p} wins!")
            return

        turn += 1

    show()
    print("Draw!")
