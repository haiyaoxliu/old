towers = [ [3,2,1], [], [] ]
print(towers)
def solve(s,i,d,t):
    #print(towers)
    if t == 1:
        #if towers[s] != [] and (towers[d] == [] or towers[s][-1] < towers[d][-1]):
        #    towers[d].append(towers[s].pop())
        print(t, s, d)
        return
    if t > 1:
        solve(s,d,i,t - 1)
        #if towers[s] != [] and (towers[d] == [] or towers[s][-1] < towers[d][-1]):
        #    towers[d].append(towers[s].pop())
        #print(towers)
        solve(i,s,d,t - 1)
print(solve(0,1,2,3))
        
    
    
#    if towers[t] != [] and (towers[p] == [] or towers[t][-1] < towers[p][-1]):
#        towers[p].append(towers[t].pop())
#       print(towers)
#   else:
#       return
#   if depth > 0:
#       hanoi(towers,t,,depth-1)
#       hanoi(towers,t,,depth-1)
#       hanoi(towers,t,p,depth-1)
#       hanoi(towers,,p,depth-1)
#   return towers
 