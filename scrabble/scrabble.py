import random

def read_dictionary():
    dictionary_file = open('dictionary.txt','r')
    dictionary = dictionary_file.read()
    dictionary_list = dictionary.split('\n')
    return dictionary_list

def filter_dictionary(dictionary_word):
    max_word_length = 7
    word_less_than_max = len(dictionary_word) <= max_word_length
    

    letters_in_word = True
    for letter in PLAYER_LETTERS:
        if letter.lower() in dictionary_word:
            continue
        else: 
            letters_in_word = False
            break
                    
    return word_less_than_max and letters_in_word


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
    letter_distribution = 'E' * 12 + ''.join(['A','I'] * 9) + 'O' * 8 + ''.join(['N','R','T'] * 6) + ''.join(['L','S','U','D'] * 4) \
    + 'G' * 3 + ''.join(['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y'] * 2) + ''.join(['K', 'J', 'X', 'Q', 'Z'] * 1)

    letter_count = 7
    for i in range(letter_count):
        chosen_letter = random.choice(letter_distribution).upper()
        player_letters.append(chosen_letter)
    return player_letters




PLAYER_LETTERS = assign_player_letters()
dictionary_list = read_dictionary()
filtered_dictionary = list(filter(filter_dictionary,dictionary_list))


print(PLAYER_LETTERS)
print(filtered_dictionary)
print(max(filtered_dictionary,key=len))
#end task
