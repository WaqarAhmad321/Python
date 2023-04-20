import random
words_list = ["goalkeeper", "hangman", "prettier", "finally", "guess", "treasure",
              "dictionary", "outline", "timeline", "online", "offline", "hello", " world"]
display = []
chosen_word = random.choice(words_list)
print(f"word is {chosen_word}")
end_of_game = None
n = 0
while n <= len(chosen_word):
    guess = ("Guess a letter : ").lower()
    for letter in chosen_word:
        if guess == letter:
            display.append(letter)
        else:
            display.append("_")
        n += 1
print(display)
