def hangman(word):
    guesses = ''
    turns = 6

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1

        if failed == 0:
            print("\nCongratulations! You guessed the word!")
            break

        guess = input("\nGuess a letter: ")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong guess! You have", turns, "turns left.")

        if turns == 0:
            print("Oops! You ran out of turns. The word was", word)

word = input("Enter a word for hangman: ")
hangman(word)
