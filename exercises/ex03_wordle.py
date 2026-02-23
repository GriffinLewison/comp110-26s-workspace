"""EX03 - Wordle - What word could it be?"""

__author__ = "730740372"


def input_guess(secret_word_len: int) -> str:
    """confirms length of guess is the same as length of secret word, returning guess."""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    
    return guess

def contains_char(secret_word: str, guess_chars: str) -> bool:
    """Function checks if the guess contains letters found in the secret word."""
    assert len(guess_chars) == 1
    #Assert statement to confirm if guess_chars is single character.
    i: int = 0
    #Defined variable i as an int equal to 0.
    while i < len(secret_word):
        #while the variable i is less than the length of the secret word, check if the guess character is in the secret word at index i.
        if secret_word[i] == guess_chars:
            return True
        i += 1
        #increase i by 1 to check the next index of the secret word.
    return False

def emojified(guessed_word: str, secret_word: str) -> str:
    """Returns green, yellow, or white boxes like Wordle based on the position and characters of guess and secret word."""
    assert len(guessed_word) == len(secret_word)
    #Assert statement to confirm guessed_word and secret_word are the same length.
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    #variables for different colored boxes like in wordle. 
    guess_result: str = ""
    #variable for string of emojis being returned.
    i: int = 0
    
    while i < len(secret_word):
        
        if guessed_word[i] == secret_word[i]:
            guess_result += GREEN_BOX
        elif contains_char(secret_word, guessed_word[i]):
            guess_result += YELLOW_BOX
        else:
            guess_result += WHITE_BOX
        i += 1
        
    return guess_result

def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    guess: str = ""
    turn: int = 1
    while turn <= 6 and guess != secret:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
        main(secret="codes")
