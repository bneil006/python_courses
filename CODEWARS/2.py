# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

def alphabet_position(text):
    alpha_position = ""

    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alpha_dict = {}
    counter = 1
    for i in alpha:
        # I didn't want to type out the entire dict "a": 1, "b": 2 and so on but idk, maybe i should have, this list took roughly the same time.
        alpha_dict[i] = counter
        counter += 1
    
    for i in text.lower():
        if i in alpha_dict:
            alpha_position += f"{str(alpha_dict[i])} "
    
    return alpha_position.strip()

    

def main():
    text, answer = "The sunset sets at twelve o' clock.", "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    if alphabet_position(text) == answer:
        print("Nice")

main()