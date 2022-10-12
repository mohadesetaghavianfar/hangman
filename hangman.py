import help_list
import random

global selected_word
global user_playground
selected_word = random.choice(help_list.words)
user_playground = "".join(['_' if char != " " else " " for char in selected_word])

def draw(wrongs):
    print(help_list.frames[wrongs])

def check_words(selected, user):
    if selected == user:
        return True
    else:
        return False

def won():
    print("You won!/n The word was ",selected_word)

def lost():
    print("You lost!/n The word was ",selected_word)

global guessed_wrong
guessed_wrong = 0
global guessed_chars
guessed_chars = []
print(user_playground)
while(guessed_wrong< 7):
    if check_words(selected_word,user_playground):
        won()
        break
    else:
        pass

    g_char = str(input("What character would you think is in word?(write and hit enter)"))

    if g_char in guessed_chars:
        print("You have guessed this character!")
        continue
    else:
        guessed_chars.append(g_char)
    replaced = 0
    for index,char in enumerate(selected_word):
        if str(char) == g_char:
            user_playground = user_playground[:index] + g_char + user_playground[index+1:]
            replaced += 1

    if replaced == 0:
        print("Wrong guess!")
        guessed_wrong += 1
        draw(guessed_wrong-1)
        continue
    else:
        print(user_playground)
else:
    lost()
