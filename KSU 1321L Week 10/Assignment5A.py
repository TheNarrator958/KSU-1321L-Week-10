# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : Assignment 5A

def extract_letters(word):
    letters = ""
    for ch in word:
        if not ch.isdigit():
            letters += ch
    return letters


def sum_digits(word):
    total = 0
    for ch in word:
        if ch.isdigit():
            total += int(ch)
    return total


def rotate_word(word, positions):
    if len(word) == 0:
        return word
    positions = positions % len(word)
    return word[positions:] + word[:positions]


def decode_word(word):
    letters = extract_letters(word)
    digit_sum = sum_digits(word)
    if has_digit(word):
        return rotate_word(letters, digit_sum)
    return letters


def has_digit(word):
    # Helper: a word containing digit 0 still counts as having digits
    for ch in word:
        if ch.isdigit():
            return True
    return False


def main():
    message = input("Enter a secret message: ")
    words = message.split()

    decoded_words = []
    modified_count = 0
    digit_word_count = 0

    for word in words:
        decoded = decode_word(word)
        decoded_words.append(decoded)

        if decoded != word:
            modified_count += 1
        if has_digit(word):
            digit_word_count += 1

    print("Decoded message:", " ".join(decoded_words))
    print("Total words modified:", modified_count)
    print("Words containing digits:", digit_word_count)


main()