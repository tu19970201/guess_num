import random

r = random.randint(1, 100)

while True:
    guess = input('猜數字1~100:')
    guess = int(guess)

    if guess > r:
        print('小一點')

    elif guess < r:
        print('大一點')

    else:
        print('終於猜對了！')
        break