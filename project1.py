'''to make a snake water gun game  mujhe vlaues deni hogi lile 1 pr 2 or 3 '''
import random
computer = random.choice([-1,0,1])
user = input('enter your choice ')
power={'snake':1,"water":-1,'gun':0}
comuterpower={1:'snake',-1:"water",0:'gun'}
showpower=power[user]
print(f'this is your  choice {user} this one is computer choice {comuterpower[computer]}')
if (comuterpower[computer]==user):
    print('its a draw')
else:
     if (computer ==1 and showpower==-1):
         print('you loss ')
     elif (computer==1 and showpower==0):
         print('you won')
     elif (computer ==-1 and showpower==0):
         print('you loss ')
     elif(computer ==-1 and showpower==1):
         print('you won ')
     elif (computer ==0 and showpower==-1):
         print('you won ')
     elif (computer == 0 and showpower==1):
         print('you loss ')
     else :
         print('something is wrong ')
