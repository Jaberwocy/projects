# Write your code here :-)
from words import words_ua, words_en
import string




alphabet_ua =set("АБВГДЄЕЖЗІИКЛМНОПРСТУФХЦЧШЩЬЮЯ")
alphabet_en = set(string.ascii_uppercase)
def choose(lang, request):
    if lang == 'U':
        words = words_ua
        alphabet = alphabet_ua
    elif lang == 'E':
        words = words_en
        alphabet = alphabet_en
    else:
        print("❌ Невідома мова! Введіть 'U' або 'E'.")
        return

    if request == 'words':
        return words
    elif request == 'alphabet':
        return alphabet

lang = input('Оберіть мову - Українська(U) Ангійська (E):' )
words=choose(lang, 'words')
alphabet=choose(lang, 'alphabet')
print(alphabet)




