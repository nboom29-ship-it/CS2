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

def reverse(word):
    reversed_word = []
    for letter in reversed(word):
        reversed_word.append(letter)

    reversed_word = "".join(reversed_word)

    print(reversed_word)

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

    print(f"You have {counter} vowels in '{word}': {acount} a's, {ecount} e's, {icount} i's, {ocount} o's, {ucount} u's. ")

def find_consonants(word):
    counter = 0
    consonants = list("bcdfghjklmnpqrstvwxyz")

    con_index = {}
    for letter in consonants:
        con_index[letter] = 0

    for letter in word:
        if letter in consonants:
            counter += 1

            con_index[letter] = con_index.get(letter) + 1

    print(f"There are {counter} consonants in '{word}': ")
    for letter in consonants:
        print(f"There are {con_index.get(letter)} {letter}'s in '{word}'. ")


    print(f"There are {counter} consonants in '{word}'. ")

def number_of(word, character):
    counter = 0

    for letter in word:
        if letter == character:
            counter += 1

    return counter

def test_for_name(word):
    while True:
        if number_of(word, " ") != 1:
            print(f"It seems '{word}' doesn't only have your first and last name in it. Please try again. ")
            word = input("What is your name? Enter your first and last name. ")
        else:
            return word

def firstname(name):
    name = test_for_name(name)

    print(f"Your first name is {name.split(' ')[0]}. ")

def lastname(name):
    name = test_for_name(name)

    print(f"Your last name is {name.split(' ')[1]}. ")

def middle_name(name):
    while True:
            if number_of(name, " ") < 2:
                print(f"It seems '{name}' doesn't only have your first name, middle name(s), and last name in it. Please try again. ")
                name = input("What is your name? Enter your first and last name. ")
            else:
                break

    print(f"Your middle name is {name.split(' ')[1].split(' ')[0]}")

def find_hyphen(word):
    word = test_for_name(word)
    last_name = word.split(" ")[1]
    found = False

    for letter in last_name:
        if letter == "-":
            found = True

    return found, last_name

def make_lowercase(word):
    lowercases = list("abcdefghijklmnopqrstuvwxyz")
    uppercases = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_word = []
    letter_combos = {}

    for llet, ulet in lowercases, uppercases:
        letter_combos[llet] = ulet


    for letter in word:
        new_word.append()

    print(word.lower())

def make_uppercase(word):
    print(word.upper())

def main():
    reverse(input("What word do you want to reverse? "))

    find_vowels(input("We'll find how many vowels you have in this word: "))

    find_consonants(input("We'll find how many consonants you have in this word: "))

    firstname(input("What is your name? Enter your first and last name. "))
    lastname(input("What is your name? Enter your first and last name. "))
    middle_name(input("What is your name? Enter your first, middle, and last name. "))

    hyphen_in, last_name = find_hyphen(input("What is your name? Enter your first and last name. "))
    if hyphen_in:
        print(f"Your lastname, {last_name} has a hypen! ")
    else:
        print(f"Your lastname, {last_name} does not have a hypen! ")

    make_lowercase(input("What word do you want to make lowercase? "))
    make_uppercase(input("What word do you want to make uppercase? "))







main()