import random

r = random.randint(1, 100)
t = 0

while True:
    guess = input('猜數字1~100:')
    guess = int(guess)
    t += 1

    if guess > r:
        print('小一點')

    elif guess < r:
        print('大一點')

    else:
        print('終於猜對了！')    
        print('你猜了第', t, '次')
        break
        
    print('你猜了第', t, '次')