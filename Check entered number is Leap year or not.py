year=int(input('Enter year'))
if(year%4==0):
  print('Year is leap year')
elif(year%400==0):
  print('Year is leap year')
else:
  print('Year is not leap year')
