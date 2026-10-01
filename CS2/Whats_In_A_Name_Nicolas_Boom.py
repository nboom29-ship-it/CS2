"""
Name: Nicolás Boom
Description: 15 functions without string functions
Bugs: None known
Date: 9/29/2026
Bonuses: Consonant frequency with subtotals for each consonant, return fullname as sorted array of characters, build a menu, return boolean if name contains a title/distinction, and my own function: the search_factors function
Log: Initial version: 9/10/2026
    9/18/2026 9:05: Updated to include reverse, find_vowels, find_consonants, get_firstname, get_lastname, make_uppercase, make_lowercase
    9/29/2026 8:50: Reverse, Find_vowels, Find_consonants, Firstname, Lastname, Middlename, Find_hyphen_in_lastname, Make_lowercase, Make_uppercase, Scramble, Find_palindrome_in_first_name, Make_array,
                Get_initials, Find_title, and Find_factors functions were included and updated
    9/29/2026 8:49: Added documentation to all functions, as well as supplementary documentation using hashtags to specific lines. Changed name of file from What_Is_In_A_Name.py to Whats_In_A_Name_Nicolas_Boom
    10/1/2026 10:55: Fixed bugs in firstname and lastname functions

"""

import random

def reverse(word):
    """
    Description: Return the reversal of the inputted word
    Uses a for loop and returns no error.

    Parameters:
    - word: the string to be reversed

    Returns:
    - reversed_word: the word after being reversed
    """
    reversed_word = []
    for letter in reversed(word):
        reversed_word.append(letter)

    reversed_word = "".join(reversed_word)

    return reversed_word

def find_vowels(word):
    """
        Description: Searches the word for vowels, and returns how many total vowels and subtototals for each one. 
        Uses a for loop and returns no errors.
    
        Parameters:
        - word: the string to be searched for vowels
    
        Returns:
        - total: total number of vowels
        - count_of_a: total number of a's
        - count_of_e: total number of e's
        - count_of_i: total number of i's
        - count_of_o: total number of o's
        - count_of_u: total number of u's
    """

    total, count_of_a, count_of_e, count_of_i, count_of_o, count_of_u = 0, 0, 0, 0, 0, 0          #sets total, count_of_a, count_of_e, count_of_i, count_of_o, and count_of_u to integer 0
    vowels = list("aeiou")

    for letter in word:
        if letter in vowels:
            total += 1

            if letter == "a":
                count_of_a += 1
            elif letter == "e":
                count_of_e += 1
            elif letter == "i":
                count_of_i += 1
            elif letter == "o":
                count_of_o += 1
            elif letter == "u":
                count_of_u += 1

    return total, count_of_a, count_of_e, count_of_i, count_of_o, count_of_u

def find_consonants(word):
    """
    Description: Searches the word for consonants, and returns the total number of consonants and subtotals for each consonant.
    Uses two for loops and returns no error.

    Parameters:
    - word: the string to be searched for consonants

    Returns:
    - total: the total amount of consonants in word
    - consonants_dict: the dictionary in which the keys are the consonants, and the values are the amount of each consonant correlated to each consonant
    """

    total = 0
    consonants = list("bcdfghjklmnpqrstvwxyz")

    consonants_dict = {}
    for letter in consonants:
        consonants_dict[letter] = 0

    for letter in word:
        if letter in consonants:
            total += 1

            consonants_dict[letter] = consonants_dict.get(letter) + 1       #adds 1 to the value associated with the key consonant_dict[letter], essentially adding 1 to the record of that consonant


    return total, consonants_dict

def number_char_in_word(word, character):
    """
        Description: Returns the number of a certain character in a certain string
        Uses a for loop and returns no error.
    
        Parameters:
        - word: the string to be searched for the character
        - character: the character to be searched for in string
    
        Returns:
        - total: the number of character in word
    """

    total = 0

    for letter in list(word):
        if letter == character:
            total += 1

    return total

def get_firstname(name):
    """
        Description: Return the first name of a string that contains a first and last name. Checks the name to make sure it only has 1 space.
        Uses a while true loop and returns no error.
    
        Parameters:
        - name: the name to be searhced for a first name
    
        Returns:
        - first_name: the first name of the inputted name
    """
    
    while True:
        if number_char_in_word(name, " ") > 1 or name[0] == " " or name[-1] == " ":
            print(f"It seems '{name}' doesn't only have your first and last name in it. Please try again. ")
            name = input("What is your name? Enter your first and last name. ")
            
        else:
            break
            

    first_name = name.split(' ')[0]

    return first_name

def get_lastname(name):
    """
        Description: Return the last name of a string that contains a first and last name. Checks the name to make sure it only has 1 space.
        Uses a while true loop and returns no error.
    
        Parameters:
        - name: the name to be searhced for a last name
    
        Returns:
        - last_name: the last name of the inputted name
    """

    
    while True:
        if number_char_in_word(name, " ") > 1 or name[0] == " " or name[-1] == " ":
            print(f"It seems '{name}' doesn't only have your first and last name in it. Please try again. ")
            name = input("What is your name? Enter your first and last name. ")
            
        else:
            break
            

    last_name = name.split(' ')[1]

    return last_name

def get_middle_name(name):
    """
        Description: Return the middle name of a string that contains a first and last name. Checks the name to make sure it only has 2 spaces.
        Uses a while true loop and returns no error.
    
        Parameters:
        - name: the name to be searhced for a middle name
    
        Returns:
        - middle_name: the middle name of the inputted name
    """
    while True:
        if number_char_in_word(name, " ") > 2 or name[0] == " " or name[-1] == " ":
            print(f"It seems '{name}' doesn't only have your first name, middle name(s), and last name in it. Please try again. ")
            name = input("What is your name? Enter your first and last name. ")
        else:
            break

    middle_name = name.split(' ')[1].split(' ')[0]          #this splits name, taking the first index of the split. Then, it takes the zero-th index after splitting that earlier value

    if middle_name == "":                                   #fixes the bug where the user enters a character, then double space in the middle, then another character
        print(f"'{name}' has a double space in the middle. Please try again:  ")
        middle_name = get_middle_name(input('What is your name? Enter your first, middle, and last name. '))        #this is a recursive call, to enable the user to try again

    return middle_name

def find_hyphen(word):
    """
        Description: Returns a boolean if there is a hyphen in word, as well as the word searched for a hyphen
        Uses a for loop and returns no error.
    
        Parameters:
        - word: the string to be searched for the hyphen
    
        Returns:
        - found: the boolean describing if a hyphen was found in word
        - word: the word in which a hyphen was searched for
    """

    found = False

    for letter in word:
        if letter == "-":
            found = True

    return found, word

def find_hyphen_in_lastname():
    """
        Description: Returns a boolean if there is a hyphen in lastname, which uses the get_lastname function to find it. Uses the find_hyphen function to search for a hyphen.
        Uses no loops and returns no error.
    
        Parameters:
        - None
    
        Returns:
        - hyphen_in: the boolean describing if there was a hyphen in last_name
        - last_name: the last_name that was searched for a hyphen
    """

    lastname = get_lastname(input("What is your name? Enter your first and last name. "))
    hyphen_in, last_name = find_hyphen(lastname)

    return hyphen_in, last_name


def make_lowercase(word):
    """
        Description: Takes a word, then converts all letters into lowercase
        Uses two for loops and returns no error.
    
        Parameters:
        - word: the string to become lowercase
    
        Returns:
        - lowercased_word: the word that became lowercase
    """
    
    lowercases = list("abcdefghijklmnopqrstuvwxyz")
    uppercases = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_word = []
    letter_combos = {}

    for i in range(len(lowercases)):
        letter_combos[uppercases[i]] = lowercases[i]            #for the dictionary letter_combos, this sets the key to uppercases[i] and the associated value to lowercases[i]

    for letter in word:
        if letter in uppercases:
            new_word.append(letter_combos.get(letter))
        else:
            new_word.append(letter)

    lowercased_word = "".join(new_word)
    
    return lowercased_word

def make_uppercase(word):
    """
        Description: Takes a word, then converts all letters into uppercase
        Uses two for loops and returns no error.
    
        Parameters:
        - word: the string to become uppercase
    
        Returns:
        - uppercased_word: the word that became uppercase
    """
    
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

    uppercased_word = "".join(new_word)

    return uppercased_word

def scramble(word):
    """
        Description: Takes a word, then switches their order, effectively scrambling the word, and returns the scrambled word
        Uses no loops and returns no error.
    
        Parameters:
        - word: the string to become scrambled
    
        Returns:
        - scrambled_word: the word that got scrambled, after being scrambled
    """
    
    new_word = list(word)
    random.shuffle(new_word)
    scrambled_word = "".join(new_word)
    return scrambled_word

def find_palindrome(word):
    """
        Description: Takes a word, then checks if it is a palindrome
        Uses no loops and returns no error.
    
        Parameters:
        - word: the string that is checked to see if it is a palindrome
    
        Returns:
        - True: the literal boolean if the word is a palindrome
        - False: the literal boolean if the wor is not a palindrome
    """
    
    if word == reverse(word):
        return True
    else:
        return False

def find_firstname_palindrome():
    """
        Description: Uses the get_firstname function to find the user's firstname, and the find_palindrome function to check that name to see if it is a palindrome
        Uses no loops and returns no error.
    
        Parameters:
        - None
    
        Returns:
        - True: the literal boolean if the user's firstname is a palindrome
        - False: the literal boolean if the user's firstname is not a palindrome
    """
    
    name = get_firstname(input("What is your name? Enter your first and last name. "))

    if find_palindrome(name):
        return True
    else:
        return False

def make_array(word):
    """
        Description: Takes a word, sorts it alphabetically, then returns the list form of that sorted array of characters where each item is a single character
        Uses a for loop and returns no error.
    
        Parameters:
        - word: the string whose characters are to be sorted and converted to list form
    
        Returns:
        - new_word: the list array of sorted characters pulled from the parameter word
    """
    
    word_list = list(word)
    lowercases = list("abcdefghijklmnopqrstuvwxyz")
    uppercases = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_word = []

    for lower_letter, upper_letter in zip(lowercases, uppercases):          #zip allows the single for loop to run through two different lists at the same time
        for letter in word:
            if letter == lower_letter or letter == upper_letter:
                new_word.append(letter)

    return new_word

def get_initials():
    """
        Description: Asks for the user's name, makes sure there is only a first and last name, then returns the user's initals
        Uses a while true loop and returns no error.
    
        Parameters:
        - None
    
        Returns:
        - initials: the user's initials
    """
    
    name = input("Enter your first and last name. ")

    while True:
        if number_char_in_word(name, " ") == 1:
            break
        else:
            print(f"It seems '{name}' doesn't only have your first and last name in it. Please try again. ")
            name = input("What is your name? Enter your first and last name. ")

    first_initial = make_uppercase(name.split(' ')[0][0])           #name.split(' ')[0][0] takes the zero-th index character of the zero-th index part of the name being splitted
    last_initial = make_uppercase(name.split(' ')[1][0])            #name.split(' ')[1][0] takes the zero-th index character of the first index part of the name being splitted
    initials = first_initial + last_initial

    return initials

def find_title(word):
    """
        Description: Searches a word for titles, returns the boolean True and the title if one was found, and only returns False if no title was found
        Uses a for loop and returns no error.
    
        Parameters:
        - word: the string to be searched for a title
    
        Returns:
        - True: the literal boolean if there was a title found in word
        - title: if there was one found, the title found in word
        - False: the literal boolean if there was no title found in word
    """
    
    titles = ["Dr.", "Sir", "Esq", "Ph.d"]

    for title in titles:
        if title in word:
            return True, title

    return False

def find_factors(number, number_range):
    """
        Description: Takes a number and a range, finds the factors of the number upto the range, and returns a boolean describing if the number if prime
        Uses a for loop and returns no error.
    
        Parameters:
        - number: the integer for which factors are found
        - number_range: the highest number checked if it is a factor of number
    
        Returns:
        - factors: the factors of number
        - is_prime: the boolean describing if number was a prime number
    """
    
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
    """
        Description: Takes a string, then that string into an integer, if it is possible. If that string is not an integer, the program will ask the user to re-input the number until it is qualifies as an integer type
        Uses a while true loop and a for loop, and returns no error.
    
        Parameters:
        - number: the string to become an integer
    
        Returns:
        - number: the string-turned-integer, or the new integer the user inputted
    """
    
    while True:
        try:
            number = int(number)
            return number
        except:
            number = input("Your number was not an integer. Please try again: ")

def main():
    while True:                                                                     #triple quotation marks take into account tab-ins and lines when printing
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
                            #the following if's and elifs are the numbers corresponding to the different options of functions the user can pick from. the last 'else:' corresponds to the invalid response message
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
            for letter in list("bcdfghjklmnpqrstvwxyz"):                                                            #displays the amount of each consonant
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
            for factor in factors_list:                     #compiles the list of integer factors into string factors of the same corresponding number
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