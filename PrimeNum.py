number = int(input("Enter Number to find Prime Number : \n"))
count = 0
for i in range(1,number+1):
    if number % i == 0:
            count = count + 1
if(count == 2):
    print(number,"is an Prime Number");
else:
    print(number,"is an Prime Number");
