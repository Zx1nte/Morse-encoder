import time


morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', ' ': ' '
    }

letter = input("Enter your sentence:  ")
chars = letter.upper()
lenght = len(chars)
print(f"your input is {lenght} letters long")
print()

for char in chars:
	print(morse.get(char), char)
	#print(letter)
print()
print(letter)
print()

qn = input("Would you like that as a sentence \"(in morse)\"? (y/n): ")
sentence = qn.lower()
print()
print()

if sentence == "y" or "yes":
	for char in chars:
		print(morse.get(char),end=" ")
	
elif sentence == "n" or "no":
	print("Alright, Thank you :) ")

print(letter)
