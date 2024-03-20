# This program takes a string and replaces a word with another word.
def replace_word():

    str = "Hi everyone, my name is Dorian. This is my Word Replacement Program. I hope you enjoy it."
    word_to_replace = input("Enter the word you want to replace: ")
    word_replacement = input("Enter the word you want to replace it with: ")

    print(str.replace(word_to_replace, word_replacement))

replace_word()