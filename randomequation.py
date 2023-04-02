import random as r
operator =[ '+' , '-' , '*' , '/' ]
#result = "{}{}{}{}{}{}{}".format(random.randint(1,10),random.choice(operator),random.randint(1,10)*x,random.choice(operator),random.randint(1,10)*x,random.choice(operator),random.randint(1,10))
while(True):
    equation = "{}{}{}{}{}{}{}".format(r.randint(1,10),r.choice(operator),r.randint(1,10),r.choice(operator),r.randint(1,10),r.choice(operator),r.randint(1,10)) # n1 op n2 op n3 op n4 
    result = round(eval(equation),2)
    print("Your Equation is {}".format(equation))
    answer = float(input("Enter your Answer :"))
    if (result == answer):
        print("You Win")
        break
    else:
        print("You Loose")
        print("Correct answer is : ",result)
        continue
    


