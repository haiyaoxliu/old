#8 queens
def solve(board,row,n):
    if check(board):
        if len(board) == n:
            print 'solution:',board
            return True
        for i in range(n):
            new = solve(board+[(row,i)],row+1,n)
            if new: return #True
    return False

def check(board):
    x = [x[1] for x in board]
    if len(board) != len(set(x)):
        return False
    for i in board:
        for j in board:
            if i != j:
                if abs(i[0] - j[0]) == abs(i[1] - j[1]):
                    return False
    return True

solve([],0,8)