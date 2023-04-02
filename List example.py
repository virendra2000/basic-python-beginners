int_list=[1,2,3]
str_list=['GUI']
list = [1, 2, 5, 4, 7, 9, 8, 6, 10, 3]
s=input("Input Character :\n")
if str(s).isdigit():
    int_list.append(int(s))
    print(int_list)
elif s.isalpha():
    str_list.append(str(s))
    print(str_list)
else:
    print('Input Character symbol')
print('Maximum of Integer List is =\n',max(int_list))
print('Minimum of Integer List is=\n',min(int_list))
list.sort(reverse=false)
print('Sorted List =\n',list)