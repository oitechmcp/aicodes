# 11. Alpha-Beta Pruning
def alpha_beta(node, depth, alpha, beta, is_max, values, height):
    if depth == height: return values[node]
    left  = 2*node+1; right = 2*node+2
    if is_max:
        v = -math.inf
        for child in [left, right]:
            v = max(v, alpha_beta(child,depth+1,alpha,beta,False,values,height))
            alpha = max(alpha, v)
            if beta <= alpha: break
        return v
    else:
        v = math.inf
        for child in [left, right]:
            v = min(v, alpha_beta(child,depth+1,alpha,beta,True,values,height))
            beta = min(beta, v)
            if beta <= alpha: break
        return v

values = [3,5,2,9,12,5,23,23]
print("Alpha-Beta:", alpha_beta(0,0,-math.inf,math.inf,True,values,3))