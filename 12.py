# 12. 8-Queens
def n_queens(n=8):
    def solve(col, placed):
        if col==n: return [list(placed)]
        solutions=[]
        for row in range(n):
            if all(placed[c]!=row and abs(placed[c]-row)!=col-c for c in range(col)):
                solutions += solve(col+1, placed+[row])
        return solutions
    sols = solve(0,[])
    print(f"8-Queens: {len(sols)} solutions, first: {sols[0]}")

n_queens()