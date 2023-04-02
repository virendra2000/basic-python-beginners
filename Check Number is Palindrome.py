num = int(input("Enter number to find Palindrome : \n"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10;
    sum = sum * 10 + digit;
    temp //= 10
if(num == sum):
    print(num,"is an Palindrome Number")
else:
    print(num,"is not an Palindrome Number")
