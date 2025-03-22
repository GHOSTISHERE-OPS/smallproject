import random 
actual_number= random.randint(1,100)
a=-1
gussees=1
while (a !=actual_number):
    a=int(input('enter the number between 1 to 100 '))
    if (a>actual_number):
        print('the lower number ')
        gussees+=1
    elif (a<actual_number):
        print('the higher number ')
print(f'the game number  is{actual_number}  and your number is {a} and the attempts you try {gussees}')

