import random


Secret_word = 'Giraffe Book Pen'
x = Secret_word.split()
Secret_word = (random.choice(x))



clue_1 = ("Your first clue is:\nI am an animal")
clue_2 = ("Your second clue is:\nI am tall")
clue_3 = ("Your third and last clue is:\nMy name starts with a G")

clue_4 = ("Your first clue is:\nI have pages")
clue_5 = ("Your second clue is:\nYou can read me")
clue_6 = ("Your third and last clue is:\nMy name starts with a B")

clue_7 = ("Your first clue is:\nI can write")
clue_8 = ("Your second clue is:\nSometimes I´m made out of ink")
clue_9 = ("Your third and last clue is:\nMy name starts with a P")


Player = input("Hi, and welcome to my guessing game!\n"
               "If you can write the secret word that I´m looking for within three guesses you win,\n"
               "but if you can´t break the secret word yo´ll loose! I will help you with some clues along the way.\n"
               "What is your name?: ")
print("Ok " + Player + ", lets see if you have what it takes, Good luck!")
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess.capitalize() != Secret_word and not out_of_guesses:
    if guess_count < 1 and Secret_word == 'Giraffe':
        print(clue_1)
    if guess_count == 1 and Secret_word == 'Giraffe':
        print(clue_2)
    if guess_count == 2 and Secret_word == 'Giraffe':
        print(clue_3)
    if guess_count < 1 and Secret_word == 'Book':
        print(clue_4)
    if guess_count == 1 and Secret_word == 'Book':
        print(clue_5)
    if guess_count == 2 and Secret_word == 'Book':
        print(clue_6)
    if guess_count < 1 and Secret_word == 'Pen':
        print(clue_7)
    if guess_count == 1 and Secret_word == 'Pen':
        print(clue_8)
    if guess_count == 2 and Secret_word == 'Pen':
        print(clue_9)
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1


    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOOSE!\nThe secret word was "+Secret_word)
else:
    print("You guessed the secret word: " + Secret_word + "\nYou win!!")
