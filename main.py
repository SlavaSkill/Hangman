# game conditions and variables
print('Hello there! Welcome to the Hangman game!')
word = str(input('Please enter your word: '))
length_of_word = len(word)
while True:
    lives = 6
    if length_of_word <= 3:
        print("Your word can't be less than 4 letters")
        word = str(input("Please try again: "))
        length_of_word = len(word)
        if length_of_word <= 3:
            continue

    else:
        print("\n" * 10)  # So that the original word is not visible in the terminal
        print('Your word is ', length_of_word, 'letters long')
        print('Word', '- ' * length_of_word)
        print('You have', lives, 'shots.')
        print("If you type 1 letter and it missed, you lost 1 life. If you try to guess whole word and didn't guess, "
              "you lost 2 lives.")
        break
# lives_lost_1 = 1
# lives_lost_2 = 2
word_by_letters = list(word)
empty_word = list(length_of_word * "-")
missed_letters = list()
guessed_letters = list()
guessed_word_set = set(word)
#  guessed_word_list = list(guessed_word_set)

# game code
while word_by_letters != guessed_letters and lives != 0:
    guess = input('Please type your letter: ')
    length_of_guess = len(guess)
    if length_of_guess == 1:
        if guess in word_by_letters:  # Is there such letter in the word
            if guess in guessed_letters:  # Checking if the letter are repeated
                print("You have already tried this letter")
            else:  # If it is not repeated, then it's guessed
                print('You guessed it! letter', guess, 'is correct!')
                guessed_letters.append(guess)
                ########################################
                # From google
                for i, j in enumerate(word_by_letters):
                    if j == guess:
                        empty_word[i] = guess
                #########################################
                print("Word:", empty_word, "\nGuess", guessed_letters, "\nMisses", missed_letters, "\nLives:", lives)
                if guessed_word_set == set(guessed_letters):  # Checking that all the letters are guessed
                    print("Congratulations! You won! The correct word was:", word, "!")
                    break

        elif guess in missed_letters:  # Checking that there was no such letters before
            print("You have already tried this letter")
            continue
        else:  # if didn't guess the letter
            lives = lives - 1
            print('The letter', guess, "is incorrect. You have left", lives, 'lives.')
            missed_letters.append(guess)
            if lives == 5:
                print("   _       ")
                print("   |       ", "Word: ", empty_word)
                print("   |       ", "Guess:", guessed_letters)
                print("   |       ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 4:
                print("   ______  ")
                print("   |       ", "Word: ", empty_word)
                print("   |       ", "Guess:", guessed_letters)
                print("   |       ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 3:
                print("   ______  ")
                print("   |    0  ", "Word: ", empty_word)
                print("   |       ", "Guess:", guessed_letters)
                print("   |       ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 2:
                print("   ______  ")
                print("   |    0  ", "Word: ", empty_word)
                print("   |    █  ", "Guess:", guessed_letters)
                print("   |    █  ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 1:
                print("   ______  ")
                print("   |    0  ", "Word: ", empty_word)
                print("   |   /█\ ", "Guess:", guessed_letters)
                print("   |    █  ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 0:
                print("   ______  ")
                print("   |    0  ", "Word: ", empty_word)
                print("   |   /█\ ", "Guess:", guessed_letters)
                print("   |    █  ", "Misses", missed_letters)
                print("   |   / \ ", "Lives:", lives)
                print("___________")
                print("Sorry, you've lost! Your life level is:", lives, "Game over!")
                break

    else:
        if guess == word:  # If guessed the word
            print("Congratulations! You won! The correct word was:", word, "!")
            break
        else:  # If didn't guess the word
            lives = lives - 2
            missed_letters.append(guess)
            print("the word is incorrect! You have left", lives, 'lives.')
            if lives == 5:
                print("   _       ")
                print("   |       ", "Word: ", empty_word)
                print("   |       ", "Guess:", guessed_letters)
                print("   |       ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 4:
                print("   ______  ")
                print("   |       ", "Word: ", empty_word)
                print("   |       ", "Guess:", guessed_letters)
                print("   |       ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 3:
                print("   ______  ")
                print("   |    0  ", "Word: ", empty_word)
                print("   |       ", "Guess:", guessed_letters)
                print("   |       ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 2:
                print("   ______  ")
                print("   |    0  ", "Word: ", empty_word)
                print("   |    █  ", "Guess:", guessed_letters)
                print("   |    █  ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 1:
                print("   ______  ")
                print("   |    0  ", "Word: ", empty_word)
                print("   |   /█\ ", "Guess:", guessed_letters)
                print("   |    █  ", "Misses", missed_letters)
                print("   |       ", "Lives:", lives)
                print("___________")
            elif lives == 0:
                print("   ______  ")
                print("   |    0  ", "Word: ", empty_word)
                print("   |   /█\ ", "Guess:", guessed_letters)
                print("   |    █  ", "Misses", missed_letters)
                print("   |   / \ ", "Lives:", lives)
                print("___________")
                print("Sorry, you've lost! Your life level is:", lives, "Game over!")
                break
print("Thanks for playing!")
