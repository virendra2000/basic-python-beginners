num = int(input("Enter a number : "))
sum = 0
temp = num
count = len(str(abs(num)))
while temp > 0:
    digit = temp % 10;
    sum += digit ** count
    temp //= 10
if(num == sum):
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number");
