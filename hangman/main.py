import random

with open('wordlist.txt', 'r') as file:
    word_list = [line.strip() for line in file]
    
word = random.choice(word_list)
guesses = []
incorrect_guesses_left = 7
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print(" ")
    
    guess = input(f"Incorrect guesses left: {incorrect_guesses_left}. Next guess: ")
    guesses.append(guess)

    if guess.lower() not in word.lower():
        print(f"Incorrect guess!")
        incorrect_guesses_left -=1
        if incorrect_guesses_left == 0:
            break
    else:
        print("Correct guess!")

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

print(f"You got it! The word was {word}") if done else print(f"Game over! The word was: {word}")
