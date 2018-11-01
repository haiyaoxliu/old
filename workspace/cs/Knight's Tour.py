moves = [ (-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2) ]

def solve(board,row,col):
    #print board
    if check(board):
        if len(board) == 64:
            print 'solution', board
            return True
        for move in moves:
            nr = row + move[0]
            nc = col + move[1]
            new = solve(board+[(row,col)],nr,nc)
            if new: return True
    return False
    
def check(board):
    for i in board:
        if i[0] < 0 or i[0] > 7 or i[1] < 0 or i[1] > 7:
            return False
    if len(board) != len(set(board)):
        return False
    return True
    
solve([],0,0)