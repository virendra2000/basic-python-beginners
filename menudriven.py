pi=3.14
print("1. Area of Triangle\n 2. Area of Circle\n 3. Area of Rectangle\n")
ch = int(input("Enter your Choice : "))
if(ch == 1):
        b=int(input("Enter Value of Base : "))
        h=int(input("\nEnter Value of Height : "))
        aot = b * h
        print("Area of Triangle is ",aot);
elif(ch == 2):
        r = int(input("Enter radius : \n"))
        aoc = pi * r * r
        print("Area of Circle is ",aoc);
elif(ch==3):
        length = int(input("Enter Value of Length : "))
        breadth = int(input("Enter Value of Breadth : "))
        aor = length * breadth;
        print("Area of Rectangle is ",arr)
else:
        print("Wrong Input")
# hello world