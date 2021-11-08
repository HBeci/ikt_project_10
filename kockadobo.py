import random
import time
asd = int(input('Hányszor pörgesse meg:  ' ))
for i in range(asd):
    x = random.randint(1,6)
    print(x) 
    time.sleep(2)

    if x ==1:
        print('0 0 0')
        print('0 @ 0')
        print('0 0 0')
    elif x ==2:
        print('0 0 0')
        print('@ 0 @')
        print('0 0 0')
    elif x ==3:
        print('0 0 @')
        print('0 @ 0')
        print('@ 0 0')
    elif x ==4:
        print('@ 0 @')
        print('0 0 0')
        print('@ 0 @')
    elif x ==5:
        print('@ 0 @')
        print('0 @ 0')
        print('@ 0 @')
    elif x ==6:
        print('@ 0 @')
        print('@ 0 @')
        print('@ 0 @')