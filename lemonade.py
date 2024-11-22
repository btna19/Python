import random


dollar=[5,10,20]
print('Bill:',random.choice(dollar))
pay=input('Enter the amount you payed:')

if random.choice(dollar)==pay:
    print('True-No Balance left')
else:
    print('False-Balance left')


