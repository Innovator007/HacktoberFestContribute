def return_change(V,C):
    d=[]
    #if V=0:
    #   return d
    for i in range(0,V+1):
        d.append(0)
    for i in range(1,V+1):
	    coinchange=100000 
	    for k in range(0,len(C)):
			if (i<C[k]):
				break
			coinchange=min(coinchange,d[i-C[k]]+1)
	    d[i]=coinchange
    return d[V]
V,n=raw_input().split(' ')
#Reading the input
V=int(V)
#Making the entered amount as integer since the change is an int
n=int(n)
C=[int(x) for x in raw_input().split(' ')]
#list of coins which are used for the coinchange
print return_change(V,C)
