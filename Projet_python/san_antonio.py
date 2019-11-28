# -*- coding: utf8 -*-

import random
import json

#--------------------------------------------------------------#
# Fonctions

# Read values form a JSON file ( it's for characters's list)
def read_values_from_json(path, key):
    values = [] # Create a new empty list
    with open(path) as f: # OPen a json file with my objects
       data = json.load(f) # Load all the contained in my file
    for entry in data:
            values.append(entry[key]) # add each item in my list
    return values # return my completed list

#--------------------------------------------------------------#
# Give a json and return a list ( it's for quotes's list)
def clean_strings(sentences):
    cleaned = []
    # Store quotes on a list. Create an empty list and add each sentence one by one
    for sentence in sentences:
        # Clean quotes from whitespace and so on
        clean_sentence = sentence.strip()
        cleaned.append(clean_sentence)
    return cleaned
    
#--------------------------------------------------------------#

# Return a random item in a list
def get_random_item_in(object_list):

    # TODO: get a random number
    rand_num = random.randint(0,len(object_list) - 1)
    
    return object_list[rand_num]

#--------------------------------------------------------------#

# Return a random value from a json file
def random_values(source_path, key):
    all_values = read_values_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return get_random_item_in(clean_values)

#--------------------------------------------------------------#
# Return a random value from a json file
def random_character():
    return random_values('characters.json', 'character')

#--------------------------------------------------------------#
def random_quote():
    return random_values('quotes.json', 'quote')

#--------------------------------------------------------------#
#--------------------------------------------------------------#

# Program interaction

def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>> {} a dit : {}".format(rand_character, rand_quote))

def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez vous une autre citation? tapper [B] pour quitter le programme.')
        choice = input(message).upper()

        if choice =='B':
            break

if __name__ == '__main__':
    main_loop()
#--------------------------------------------------------------#


# if user_answer == "B":

#     pass

# elif user_answer == "C":

#     print("C pas la bonne réponse ! Et G pas d’humour, je C...")

# else:

#     # show another quote

#     pass
