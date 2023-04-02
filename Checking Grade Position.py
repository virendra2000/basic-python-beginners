per=float(input('Enter your percentage'))
if(per>=75):
    print('Congratulation ! Distinction pass')
elif(per>=60):
    print('Congratulation ! First class Pass')
elif(per<60):
    print('Second class Pass')
elif(per<40):
    print('Fail')
else:
    print('Entered Wrong Percentage')
