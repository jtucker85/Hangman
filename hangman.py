import random
import string
from hangmanvis import lives_visual_dict

fh = open("wordlist.txt")
wordlist = list()
for w in fh:
    wordstr = w.rstrip()
    wordlist.append(wordstr)
wordgen = random.choice(wordlist).upper()



def hangman():
    
    word_letters = set(wordgen)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        word_list = [letter if letter in used_letters else "-" for letter in wordgen]
        print(lives_visual_dict[lives])
        print("Current word: "," ".join(word_list))

        print(f"You have {lives} lives left and you have used these letters:"," ".join(used_letters))
        userinput = input("Choose a letter: ").upper()
        user_letter = userinput.upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print(f"Sorry, {user_letter} is not in the word.")
                print('')

        else:
            print("You've already used that letter.")
            print('')

    if lives == 0:
        print(f"Oops, you died. The word was {wordgen}")

    if len(word_letters) == 0:
        print(f"Congratulations! You got the word, it was {wordgen}")

if __name__ == '__main__':
    hangman()