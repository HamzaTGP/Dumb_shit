import random
n = random.randint(1,10)
print(n)


g = int(input('Enter your number here: '))

'''
if g == n:
    print("You guessed correct!")
else:
    print("You guessed incorrect!")
'''

while n != g:
    int(input("You guessed incorrectly! Try again: "))
    if n == g:
        print("You guessed correctly!")
        break