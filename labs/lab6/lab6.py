"""
Name: <Madison Byrne>
<Lab6>.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    names = input("Enter name: ")
    name = names.split(" ")
    print(",".join(name))

def company_name():
    x = input("Enter a website: ")
    x = x.split(".")
    print(x[1])



def initials():
    n = eval(input("Enter the amount of names there are: "))
    for i in range(n):
        first = input("Enter a value for the first name" + str(i + 1))
        last = input("Enter a value for the last name" + str (i + 1))
        initials = first[0] + last[0]
        print(first + " intials are", initials)

def names():
    names = input("Enter names:")
    names = names.split(",")
    for name in names:
        name = name.split(" ")
        first = name[0]
        last = name[1]
        print(first[0] + last[0])


def thirds():
    sentence = input("Enter a sentence")
    print(sentence[2::3])


def word_average():
    acc = 0
    sentence = input("input your sentence: ")
    sentence = sentence.split("list of words")
    for word in sentence:
        acc += len(word)
    print(acc / len(sentence))


def pig_latin():
    sentence = input("input your sentence: ")
    sentence = sentence.lower()
    sentence = sentence.split(" ")
    for word in sentence:
        x = word[1:] + word[0] + "ay"
        print(x, end=" ")

def main():
#     name_reverse()
#     # add other function calls here
#     company_name()
#     initials()
#     names()
    thirds()
    word_average()
    pig_latin()

main()





