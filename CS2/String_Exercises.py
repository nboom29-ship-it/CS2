name = "Nico"

for letter in reversed(name):
    print(letter)

fruit = "banana"
print(fruit[:])                 #[:] means the whole string


def count(word, character):
    count = 0
    for letter in word:
        if letter == character:
            count = count + 1
    print(count)


def count_letter(letter):
    print("banana".count(letter))


count(input("What word? "), input("What letter? "))
count_letter(input("What letter do you want to find in 'banana'? "))

def dice():
    str = 'X-DSPAM-Confidence: 0.8475'

    number_str = str.split(" ")[1]

    number = float(number_str)

    print(number)

dice()


