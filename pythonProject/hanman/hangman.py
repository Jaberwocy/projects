# Write your code here :-)
import random
from words import words_ua, words_en
from hangman_visual import lives_visual_dict
import string


alphabet_ua = set("АБВГДЄЕЖЗІИКЛМНОПРСТУФХЦЧШЩЬЮЯ")
alphabet_en = set(string.ascii_uppercase)
def choose(lang, request):
    if lang == '1':
        words = words_ua
        alphabet = alphabet_ua
    elif lang == '2':
        words = words_en
        alphabet = alphabet_en
    else:
        print("❌ Невідома мова! Введіть '1' або '2'.")
        return

    if request == 'words':
        return words
    elif request == 'alphabet':
        return alphabet


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    lang = input('Оберіть мову - Українська(1) Ангійська (2):' )
    words=choose(lang,'words')
    alphabet = choose(lang, "alphabet")
    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()


    lives = 7

    while len(word_letters) >0 and lives >0:
        print("У вас",lives, "спроб і ви вже використали ці літери: ", ' '.join(used_letters))


        word_list = [letter if letter in used_letters else '-' for letter in word]
        print (lives_visual_dict[lives])
        print('Задумане слово:', ' '.join(word_list))

        user_letter = input('Обери літеру: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives-1
                print('\n Ваша літера', user_letter, 'відсутня в слові')

        elif user_letter in used_letters:
            print('\n Ви вже використовували цю літеру. Задумайте іншу.')

        else:
            print('\n Це неправильна літера')

    if lives ==0:
        print(lives_visual_dict[lives])
        print('Ви вмерли. Було загадано слово', word, '!!')
    else:
        print('УРА! Ви вгадали слово', word, '!!')

    onemore = input("Зіграємо ще раз?(1 - Так, 2 - Ні): ")

    if onemore == '1':
        hangman()
    else:
        print('Гарного дня!!')


if __name__ == '__main__':
    hangman()


