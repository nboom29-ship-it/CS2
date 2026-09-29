'''
List of Functions:
1. Reverse and display
2. Determine the number of vowels. You can prompt user for a particular vowel or
create subtotals of each.
3. Consonant frequency. Bonus: Subtotals of each consonant
4. Return first name.
5. Return last name.
6. Return middle name(s)
7. Return boolean if last name contains a hyphen
8. Function to convert to lowercase
9. Function to convert to uppercase
10. Modify array to create a random name (mix up letters)
11. Return boolean if first name is a palindrome
12. Return full-name as a sorted array of characters (Bonus)
13. Build a menu (Bonus)
14. Make initials from name
15. Return boolean if name contains a title/distinction (“Dr.”, “Sir”, “Esq”, “Ph.d”)
(Bonus)
17. COME UP WITH YOUR OWN! (Bonus)
18. Secret Bonus ---See me
NOTE: For full credit, your code must be documented,
properly indented, and declarations should be a the top
'''


import random

def reverse(word):
    reversed_word = []
    for letter in reversed(word):
        reversed_word.append(letter)

    reversed_word = "".join(reversed_word)

    return reversed_word

def find_vowels(word):
    counter, acount, ecount, icount, ocount, ucount = 0, 0, 0, 0, 0, 0
    vowels = list("aeiou")

    for letter in word:
        if letter in vowels:
            counter += 1

            if letter == "a":
                acount += 1
            elif letter == "e":
                ecount += 1
            elif letter == "i":
                icount += 1
            elif letter == "o":
                ocount += 1
            elif letter == "u":
                ucount += 1

    return counter, acount, ecount, icount, ocount, ucount

def find_consonants(word):
    total = 0
    consonants = list("bcdfghjklmnpqrstvwxyz")

    consonants_dict = {}
    for letter in consonants:
        consonants_dict[letter] = 0

    for letter in word:
        if letter in consonants:
            total += 1

            consonants_dict[letter] = consonants_dict.get(letter) + 1


    return total, consonants_dict

def number_char_in_word(word, character):
    counter = 0

    for letter in list(word):
        if letter == character:
            counter += 1

    return counter

def get_firstname(name):
    while True:
        if number_char_in_word(name, " ") == 1:
            break
        else:
            print(f"It seems '{name}' doesn't only have your first and last name in it. Please try again. ")
            name = input("What is your name? Enter your first and last name. ")

    return name.split(' ')[0]

def get_lastname(name):
    while True:
        if number_char_in_word(name, " ") == 1:
            break
        else:
            print(f"It seems '{name}' doesn't only have your first and last name in it. Please try again. ")
            name = input("What is your name? Enter your first and last name. ")

    return name.split(' ')[1]

def get_middle_name(name):
    while True:
        if number_char_in_word(name, " ") < 2:
            print(f"It seems '{name}' doesn't only have your first name, middle name(s), and last name in it. Please try again. ")
            name = input("What is your name? Enter your first and last name. ")
        else:
            break

    return name.split(' ')[1].split(' ')[0]

def find_hyphen(word):
    found = False

    for letter in word:
        if letter == "-":
            found = True

    return found, word

def find_hyphen_in_lastname():
    lastname = get_lastname(input("What is your name? Enter your first and last name. "))
    hyphen_in, last_name = find_hyphen(lastname)

    return hyphen_in, last_name


def make_lowercase(word):
    lowercases = list("abcdefghijklmnopqrstuvwxyz")
    uppercases = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_word = []
    letter_combos = {}

    for i in range(len(lowercases)):
        letter_combos[uppercases[i]] = lowercases[i]

    for letter in word:
        if letter in uppercases:
            new_word.append(letter_combos.get(letter))
        else:
            new_word.append(letter)

    return "".join(new_word)

def make_uppercase(word):
    lowercases = list("abcdefghijklmnopqrstuvwxyz")
    uppercases = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_word = []
    letter_combos = {}

    for i in range(len(lowercases)):
        letter_combos[lowercases[i]] = uppercases[i]

    for letter in word:
        if letter in lowercases:
            new_word.append(letter_combos.get(letter))
        else:
            new_word.append(letter)

    return "".join(new_word)

def scramble(word):
    new_word = list(word)
    random.shuffle(new_word)
    return "".join(new_word)

def find_palindrome(word):
    if word == reverse(word):
        return True
    else:
        return False

def find_firstname_palindrome():
    name = get_firstname(input("What is your name? Enter your first and last name. "))

    if find_palindrome(name):
        return True
    else:
        return False

def make_array(word):
    word_list = list(word)
    lowercases = list("abcdefghijklmnopqrstuvwxyz")
    uppercases = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_word = []

    for lower_letter, upper_letter in zip(lowercases, uppercases):
        for letter in word:
            if letter == lower_letter or letter == upper_letter:
                new_word.append(letter)

    return new_word



def get_initials():
    name = input("Enter your first and last name. ")

    while True:
        if number_char_in_word(name, " ") == 1:
            break
        else:
            print(f"It seems '{name}' doesn't only have your first and last name in it. Please try again. ")
            name = input("What is your name? Enter your first and last name. ")

    first_initial = name.split(' ')[0][0]
    last_initial = name.split(' ')[1][0]

    return make_uppercase(first_initial) + make_uppercase(last_initial)

def find_title(word):
    titles = ["Dr.", "Sir", "Esq", "Ph.d"]

    for title in titles:
        if title in word:
            return True, title

    return False

def find_factors(number, number_range):
    factors = []
    is_prime = False

    for digit in range(number_range + 1):
        if digit != 0:
            divided_number = number / digit
            if divided_number == int(divided_number):
                factors.append(digit)

    if factors[1] == number:
        is_prime = True
    
    return factors, is_prime

def convert_to_integer(number):
    while True:
        try:
            number = int(number)
            return number
        except:
            number = input("Your number was not an integer. Please try again: ")

def main():
    while True:
        choice = input("""
Which function do you want to use? (enter the associated number)
1000: literally executes all functions in order
0: exits all code
1: Reverse
2: Find_vowels
3: Find_consonants
4: Firstname
5: Lastname
6: Middlename
7: Find_hyphen_in_lastname
8: Make_lowercase
9: Make_uppercase
10: Scramble
11: Find_palindrome_in_first_name
12: Make_array
13: Get_initials
14: Find_title
15: Find_factors
Enter here: """)

        if choice == '1000':
            print("Here are all the functions below, in the same order as seen above in the options: ")

            print(f"Your reveresed word is: '{reverse(input('What word do you want to reverse? '))}'")

            vowels = ["vowel"] + list("aeiou")
            for vowel_number, vowel_name in zip(find_vowels(input("We'll find how many vowels you have in this word: ")), vowels):
                print(f"There are {vowel_number} {vowel_name}'s. ")

            total_consonants, consonants_dict = find_consonants(input("We'll find how many consonants you have in this word: "))
            print(f"You have {total_consonants} consonants in your word. ")
            for letter in list("bcdfghjklmnpqrstvwxyz"):
                print(f"There are {consonants_dict.get(letter)} {letter}'s in your word. ")

            print(f"Your first name is: {get_firstname(input('What is your name? Enter your first and last name. '))}")

            print(f"Your lastname is: {get_lastname(input('What is your name? Enter your first and last name. '))}")

            print(f"Your middle name is: {get_middle_name(input('What is your name? Enter your first, middle, and last name. '))}")

            hyphen_in, last_name = find_hyphen_in_lastname()
            if hyphen_in:
                print("There is a hyphen in your last name! ")
            else:
                print("There is no hyphen in your last name. ")

            print(f"Here's your word in lowercase: {make_lowercase(input('What word do you want to make lowercase? '))}")

            print(f"Here's your word in uppercase: {make_uppercase(input('What word do you want to make uppercase? '))}")

            print(f"Here's your scrambled word: {scramble(input('What word do you want to scramble? '))}")

            firstname_palindrome_bool = find_firstname_palindrome()
            if firstname_palindrome_bool:
                print("Your first name is a palindrome! ")
            else:
                print("Your first name is not a palindrome. ")

            print(f"Your name as an array is: {make_array(input('What is your name? '))}")

            print(f"Your initials are: {get_initials()}")

            title_in, title_found = find_title(input('What name/word do you want to search for titles? '))
            if title_in:
                print(f"There was a title found in your word, and it was '{title_found}'. ")
            else:
                print(f"There was no title found in your word. ")

            factors_list, is_prime = find_factors(convert_to_integer(input("What number do you want to search for factors in? ")), convert_to_integer(input("What do you want the highest factor searched for to be? ")))
            factors_string_list = []
            for factor in factors_list:
                factors_string_list.append(str(factor))
            if is_prime:
                print("Your number is prime! ")
            else:
                print(f"Your factors for the above number are: {', '.join(factors_string_list)}")

        elif choice == '0':
            print("Exiting... ")
            break

        elif choice == '1': 
            print(f"Your reveresed word is: '{reverse(input('What word do you want to reverse? '))}'")

        elif choice == '2': 
            vowels = ["vowel"] + list("aeiou")
            for vowel_number, vowel_name in zip(find_vowels(input("We'll find how many vowels you have in this word: ")), vowels):
                print(f"There are {vowel_number} {vowel_name}'s. ")

        elif choice == '3':
            total_consonants, consonants_dict = find_consonants(input("We'll find how many consonants you have in this word: "))
            print(f"You have {total_consonants} consonants in your word. ")
            for letter in list("bcdfghjklmnpqrstvwxyz"):
                print(f"There are {consonants_dict.get(letter)} {letter}'s in your word. ")

        elif choice == '4': 
            print(f"Your first name is: {get_firstname(input('What is your name? Enter your first and last name. '))}")

        elif choice == '5': 
            print(f"Your lastname is: {get_lastname(input('What is your name? Enter your first and last name. '))}")

        elif choice == '6': 
            print(f"Your middle name is: {get_middle_name(input('What is your name? Enter your first, middle, and last name. '))}")

        elif choice == '7': 
            hyphen_in, last_name = find_hyphen_in_lastname()

            if hyphen_in:
                print("There is a hyphen in your last name! ")
            else:
                print("There is no hyphen in your last name. ")

        elif choice == '8': 
            print(f"Here's your word in lowercase: {make_lowercase(input('What word do you want to make lowercase? '))}")

        elif choice == '9': 
            print(f"Here's your word in uppercase: {make_uppercase(input('What word do you want to make uppercase? '))}")

        elif choice == '10': 
            print(f"Here's your scrambled word: {scramble(input('What word do you want to scramble? '))}")
        
        elif choice == '11':
            firstname_palindrome_bool = find_firstname_palindrome()

            if firstname_palindrome_bool:
                print("Your first name is a palindrome! ")
            else:
                print("Your first name is not a palindrome. ")

        elif choice == '12':
            print(f"Your name as a sorted array is: {make_array(input('What is your name? '))}")

        elif choice == '13':
            print(f"Your initials are: {get_initials()}")

        elif choice == '14':
            title_in, title_found = find_title(input('What name/word do you want to search for titles? '))

            if title_in:
                print(f"There was a title found in your word, and it was '{title_found}'. ")
            else:
                print(f"There was no title found in your word. ")

        elif choice == '15':
            factors_list, is_prime = find_factors(convert_to_integer(input("What number do you want to search for factors in? ")), convert_to_integer(input("What do you want the highest factor searched for to be? ")))
            factors_string_list = []
            for factor in factors_list:
                factors_string_list.append(str(factor))

            if is_prime:
                print("Your number is prime! ")
            else:
                print(f"Your factors for the above number are: {', '.join(factors_string_list)}")

        else:
            print("Invalid Response. Please try again below:")

        input("Hit enter to continue... ")

        print("\n")

        
    


main()