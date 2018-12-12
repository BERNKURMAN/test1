#imports random function
import random
#asks how many cards they want
x = input('How many cards do you want? 1, 2, or 0' + '\n')
print (x)

#sets card library
cards = ['Ace','Jack',
         'Queen','King',
         '2','3','4','5',
         '6','7','8','9',
         '10']
#chooses cards
card1 = random.choice(cards)
card2 = random.choice(cards)
#prints cards, showing they are the same each time
print(card1, card2)
print(card2)
print(card1)
print(card2)
print(card1)
print(card2)

card1 = random.choice(cards)
card2 = random.choice(cards)
print(card1, card2)
print ("card 1: " + card1, "\n"+ "card 2: " + card2)
print("__________________________________________________________")
print("card 1: " + card1 + "\ncard 2: " + card2)
