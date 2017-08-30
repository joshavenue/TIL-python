import random                           //  Import random library //                         
import os                               //  Import OS library //

words = [                               // Create a list of words //
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapfruit',
    'lemon',
    'blueberry',
    'melon',
]

def clear():                            // Clear() function allows the program to clear it's screen without leaving mess behind //
    if os.name == 'nt':                 // 'nt' stands for Windows OS
        os.system('cls')                // 'cls' is for Windows OS
    elif os.name == 'posix':            // 'posix' stands for MacOS
        os.system('clear')              // 'clear' is for MacOS
    else:
        pass

def draw(bad_guesses,good_guesses,secret_word):       // Draw() function takes 3 arguments
    clear()                                           // Clears screen

    print('Strikes: {}/7'.format(len(bad_guesses)))   // Prints out the number of guesses left after wrong attempts //
    print('')                                         // Empty space

    for letter in bad_guesses:                        // For any wrong guesses(word) you typed in, it will be printed on screen //
        print(letter, end=' ')                        // end= ' ' creates a spacing between print instead of creating a new line //
    print('\n\n')                                     // This separates the wrong guesses on the upper screen without overlapping the blank spaces //

    for letter in secret_word:                        // For any guesses that you typed in that has a matching letter //
        if letter in good_guesses:                    // If the letter typed in is within the matching word, it will print out the letter //
            print(letter, end=' ')
        else:
            print('_', end=' ')

    print('')

def get_guess(bad_guesses, good_guesses):             // Get_guess() function prompts the user to enter a letter, it has 2 arguments//
    while True:                                       // While True loops forever till condition is met //
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:                           // If the similar word that has been input before, it will print the error message //
            print("You've already guess that letter!")

        elif guess in bad_guesses or guess in good_guesses:    // If you have typed the letter before, it will alert you //
            print("You've already guess that letter!")

        elif not guess.isalpha():                     // guess.isalpha() is a method that check the input, if it's other than letters, error message will be alerted //
            print("You can only guess letters!")

        else:
            return guess                              // All condition favors, will pass into the list //


def play(done):                                       // Play() for the play to start //
    clear()                                           // Clear screen again //
    secret_word = random.choice(words)                // The secret_word pick a random words from the words' list declared //
    bad_guesses = []                                  // Bad_guesses is a variable with empty list, it is used for wrong guesses //
    good_guesses = []                                 // Good_guesses is a variable 

    while True:
        draw(bad_guesses, good_guesses, secret_word)  // Goes back to the draw function with the 3 argument //
        guess = get_guess(bad_guesses, good_guesses)  // Guess goes back to the get_guess() function with 2 argument //


        if guess in secret_word:                      // If the input letter is one of the secret word //
            good_guesses.append(guess)                // It will take the letter and add into the good_guesses list //
            found = True                              // A new variable 'found' will be declared True //
            for letter in secret_word:                // For any letter that is within the secret_word //
                if letter not in good_guesses:        // If that letter is not part of good_guesses //
                    found = False                     // found will be False //
            if found:                                 // if 'found' is True //
                print("You win!")                   
                print("The secret word was {}".format(secret_word))
                done = True                           // A new variable 'Done' be will declared True //
        else:
            bad_guesses.append(guess)                           // Or else, the wrong letter will go into the bad_guesses list //
            if len(bad_guesses) == 7:                           // If you guess up to 7 wrong guesses //
                draw(bad_guesses, good_guesses, secret_word)    // It will take information from draw() function //
                print("You lost!")                              
                print("The secret word was {}".format(secret_word))
                done = True                                     // Done will be True //

        if done:                                                // If done is True //
            play_again = input("Play again? Y/n ").lower()      // Askes you if you want to play again //
            if play_again != 'n':                               // If you typed anything but 'n', you will play again //
                return play(done=False)                         // done will be False //
            else:
                raise SystemExit                                // Exit the program //

def welcome():
    start = input("Press enter/return to start or Q to quit").lower()
    if start == 'q':
       print("Bye!")
       raise SystemExit
    else:
        return True



print('Welcome to Letter Guess!')

done = False

while True:
    clear()
    welcome()
    play(done)
