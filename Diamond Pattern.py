n = 3
for i in range(n):
    print(' '*(n-i-1) + '*'*((2*i)+1) )
for i in range(n):
    print(' '*(i+1) + '*'*((2*((n-1)-i))-1))
