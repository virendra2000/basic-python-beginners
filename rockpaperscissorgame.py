import random
option = ['rock','paper','scissors']
computer = random.choice(option)
gamesystem = random.choice(option)
print("Lets Play the Game")
choose = input("Please Enter any one option from rock paper scissors : \n")
if gamesystem == choose and gamesystem == computer:
    print("Yaar Computer aur Aapne ek hi option select kiya tha , Ab to match tie hogaya")
elif gamesystem==choose and gamesystem!=computer:
    print("Yaar Computer ne ",computer,"option select kiya hai , Congrats Aap Jeet Gaye  aapne ",gamesystem,"select kiya")
else:
    print("Sorry bro , Aap Nahi jeet paye aapko naa ",gamesystem,"select karna chahiye tha aur aapne kya select kiya",choose)

