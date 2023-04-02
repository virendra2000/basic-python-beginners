print("Enter the marks of 5 Subjects \n")
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
sum=float(m1+m2+m3+m4+m5)
avg=sum/5
per=round((sum/500)*100,2)

if(per>=75 and per<=100):
    print("Distinction Passed")
elif(per>=60 and per<75):
    print("First Class Passed")
elif(per>=40 and per <60):
    print("Second Class")
else:
    print("Fail")
