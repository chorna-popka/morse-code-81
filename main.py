from codetable import morse_table

print("--..-..-- WELCOME TO MORSE 1.0 --..-..--")
print("--..- enter exit to leave the program -..--")


def convert(text):
    morse_text = "   ".join([morse_table[char.upper()] for char in text])
    print(morse_text)


def run():
    to_convert = input("Please enter a string to convert in Morse: ")
    if to_convert.lower() != "exit":
        convert(to_convert)
        run()


run()