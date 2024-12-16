# Correct version
def remove_all_from_string(word, letter):
    while True:
        index = word.find(letter) 
        if index == -1:  
            return word
        word = word[:index] + word[index + len(letter):]

word = input("Enter the word: ")
letters_to_remove = input("Enter the letters to remove: ")

print("Result after removing all occurrences:", remove_all_from_string(word, letters_to_remove))
