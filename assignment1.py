import random

def guess_the_word(name):   
    word_to_guess = ["apple", "banana", "cake", "melon", "orange", "raisin", "ice cream"]
    selected_word = random.choice(word_to_guess)
    attempts = 5
    trials  = 0
    print(f"Welcome {name} to the guess the word game")
    print (f"I have selected a random word from {word_to_guess} can you tell me which is it?")
    
    while attempts >0:
       
        guess = input("Guess the word: ").lower()
        if guess not in word_to_guess:
            print("Invalid guess. Please choose from the list given")
            print(f"Available words are {word_to_guess}")
            continue
        if guess == selected_word:
            print (f"Congratulation! You have guessed the word correctly after {trials} attempts.")
            break
        if attempts ==0:
            print (f"Sorry you have run out of attempts. The word selected was '{selected_word}'")
            break
        if attempts <= 2:
            attempts -=1 
            trials +=1
            print (f"Incorrect guess. The first letter of the word is {selected_word[0]}") 
            print (f"You have {attempts} attempts remaining")
            continue
        else:
            print (f"You have {attempts} attempts remaining")
            continue



      
guess_the_word("Carol")



