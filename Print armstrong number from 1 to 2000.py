for i in range(1,2000+1):
        num = i
        temp = num
        sum = 0
        count = len(str(abs(num)))
        while temp > 0:
                digit = temp % 10
                sum += digit ** count
                temp //= 10
        if(num == sum):
                print(num)
