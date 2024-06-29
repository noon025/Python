"""
NATO system : each letter of your name mentioned to known word in special system
"""

#writing the system as dictionary 
nato = {"A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K":"Kilo", "L": "Lima", "M": "Mike", "N": "November","O": "Oscar", "P": "Papa", "Q": "Quebec", "R":"Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray","Y": "Yankee", "Z": "Zulu"}

#print name of the system 
print("========================\n NATO Phonetic Alphabet\n========================")

#variable to enter username and make it capitale letters to matches with keys of dictionary
word = input("Please enter your name: ").upper()

print("The spilling of your name phonetically is: ")

#create loop to enter in name and take each letter to call value(known word) of the letters 
for letter in word:
  if letter in nato:
    print(f"{letter}: {nato[letter]}")

  #if he found space between names, print dashes
  elif letter == " ":
    print("----")

  #if he found any thing without nato system, print same thing without change any thing
  else:
    print(f"{letter}: {letter}")
