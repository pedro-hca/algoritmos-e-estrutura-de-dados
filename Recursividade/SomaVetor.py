def Soma_elem(V, N):
    if (N == 0):
        return V[N]
    else:
        return (V[N] + Soma_elem(V, N-1))
    
V=[2,10,5,7,8,11]
N=len(V)
print(Soma_elem(V, N-1))