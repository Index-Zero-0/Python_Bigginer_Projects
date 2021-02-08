import sys


def countWord(text):
    listOfWords = text.split(" ")
    return len(listOfWords)


def countChar(text):
    listOfWords = text.split(" ")
    # Deleting spaces between words
    textWithoutSpace = "".join(listOfWords)
    return len(textWithoutSpace)


def countASpecialWord(theWord, text):
    countOfTheWord = 0
    listOfWords = text.split(" ")
    for word in listOfWords:
        if word == theWord:
            countOfTheWord += 1

    return countOfTheWord


def showOptions():
    print("""\n
            1. count of words in the text
            2. count of characters in the text (without spaces)
            3. count how many times a word is repeated in the text
            4. change the text
            5. show options
            99. exit
        """)


def main():
    text = input("Your text: ")
    showOptions()
    while True:
        usersChoose = input("\nWhat do you want to do?(write the number of the option you want)\n#")
        if usersChoose == "1":
            print("\n\nCount of words: " + str(countWord(text)) + "\n\n")

        elif usersChoose == "2":
            print("\n\nCount of characters: " + str(countChar(text)) + "\n\n")

        elif usersChoose == "3":
            theWord = input("\nWrite the word you want to count:\n#")
            timesRepeated = countASpecialWord(theWord, text)
            print("\nThe '" + theWord + "' was repeated " + str(timesRepeated) + " times in the text\n")

        elif usersChoose == "4":
            text = input("\nYour text: ")

        elif usersChoose == "5":
            showOptions()

        elif usersChoose == "99":
            sys.exit(0)
        else:
            print("\nInvalid input\n")


if __name__ == "__main__":
    main()
