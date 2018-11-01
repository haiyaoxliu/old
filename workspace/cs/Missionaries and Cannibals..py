moves = [ (2,0,1), (1,0,1), (1,1,1), (0,1,1), (0,2,1) ]
missionaries = 0
cannibals = 1
boat = 2

def solve(state, path):
    if state == [0,0,-1]:
        print 'solution:',path+[state]
        return True
    elif check(state,path):
        for move in moves:
            new = solve([state[missionaries] - state[boat] * move[missionaries],
                         state[cannibals] - state[boat] * move[cannibals],
                         -state[boat]],
                         path + [state] )
            if new: return True
    return False

def check(state,path):
    if state in path: return False
    elif state[cannibals] > state[missionaries] > 0 or 3 - state[cannibals] > 3 - state[missionaries] > 0: return False
    elif state[cannibals] > 3 or state[cannibals] < 0 or state[missionaries] > 3 or state[missionaries] < 0: return False
    else:
        return True

solve([3,3,1],[])