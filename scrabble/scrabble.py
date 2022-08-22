import string
import random

def points_for_letter(letter):
    letter_dict = {'E':1, 'A':1, 'I':1, 'O':1, 'N':1, 'R':1, 'T':1, 'L':1, 'S':1, 'U':1,'D':2,'G':2,
    'B':3,'C':3,'M':3,'P':3,'F':4,'H':4,'V':4,'W':4,'Y':4,'K':5,'J':8,'X':8,'Q':10,'Z':10}  

    letter_points = letter_dict.get(letter.upper())
    return letter_points


def points_for_word(word):
    points_for_word = 0
    for letter in word:
        points_for_word += points_for_letter(letter) 
    return points_for_word


def assign_player_letters():
    player_letters = []
    alphabet = string.ascii_letters
    for i in range(7):
        chosen_letter = random.choice(alphabet).upper()
        player_letters.append(chosen_letter)
    return player_letters

print(points_for_letter('w'))
print(points_for_word('WALL'))
print(assign_player_letters())