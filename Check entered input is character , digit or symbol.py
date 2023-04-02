k=input('Enter Character')
if((k.isalpha()) or (k.isdigit())):
   if((k>='a' and  k<='z') or (k>='A' and k<='Z')):
       j=k.swapcase()
       print('Original character is ',k)
       print('Converted Character is ',j)
   elif(k>='0' and k<='9'):
       print('Enter character is digit , so cannot convert it')
else:
       print('Invalid Character/Symbol')           

