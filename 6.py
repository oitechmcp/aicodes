# 6. Tic-Tac-Toe
def tic_tac_toe():
    board = [' ']*9
    def show(): [print(board[i],'|',board[i+1],'|',board[i+2]) for i in [0,3,6]]
    def win(p): return any(all(board[i]==p for i in c) for c in
                           [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]])
    for turn in range(9):
        show(); p = 'X' if turn%2==0 else 'O'
        move = int(input(f"{p}'s turn (0-8): "))
        if board[move]==' ': board[move]=p
        if win(p): show(); print(f"{p} wins!"); return
    show(); print("Draw!")