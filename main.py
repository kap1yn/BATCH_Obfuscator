from data import *
from itertools import permutations
import random


def get_file_content(INPUT_PATH):
    try:
        with open(INPUT_PATH, 'r') as file:
            return file.read()

    except FileNotFoundError:
        print("File not found")


def get_key_letters():
    all_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    random.shuffle(all_letters)
    return all_letters
   

def set_key():
    try:
        with open(TEMPLATE_PATH, 'r') as file:
            new_content = file.read()

    except FileNotFoundError:
        print("File not found")
    

    with open(OUTPUT_PATH, 'w') as file:
        new_content = new_content.replace("Set key=THERE_WILL_BE_NEW_KEY", f"Set key={KEY}")
        file.write(new_content)


def obfuscate_code(KEY_LETTERS, file_content):
    global buffer
    buffer = '\n'

    def get_letter_id(letter):
        return KEY_LETTERS.index(letter)
    
    def make_change(letter):
        global buffer
        try:
            letter_id = get_letter_id(letter)
            template = f'%key:~{letter_id},1%'
            buffer += template
        except ValueError:
            buffer += letter

    for char in file_content:
        make_change(char)

    with open(OUTPUT_PATH, 'a') as file:
        try:
            file.write(buffer)

        except FileNotFoundError:
            print("File not found")
            
        except Exception as error:
            print(f"Error in {error}")
        
        
if __name__ == '__main__':
    file_content = get_file_content(INPUT_PATH)

    KEY_LETTERS = get_key_letters()
    KEY = ''.join(str(item) for item in KEY_LETTERS)
    set_key()
    obfuscate_code(KEY_LETTERS.copy(), file_content)
    