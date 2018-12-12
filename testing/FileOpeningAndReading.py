import random
import os

print(os.getcwd())
os.chdir('E:/Code Writing/Python/BlackJack Game testing')
print(os.getcwd())

with open('cards.txt', 'r') as cards:
    print (cards.read())

print ('file name: ' + cards.name,
       'mode: ' + cards.mode)
print (cards.mode)



    # OS file directory Change:
import os
os.chdir('E:/*folder*/*folder*/*folder*')
    # To test directory(dir) path:
print(os.getcwd())
