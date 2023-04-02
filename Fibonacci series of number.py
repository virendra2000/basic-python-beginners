a,b = 0,1
n = int(input("Enter Number to find fibonacci series : "))
print(a)
print(b)
for i in range(0,n+1):
	c = a + b
	print(c)
	a = b
	b = c
