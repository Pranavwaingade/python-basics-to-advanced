
Sentence=input("Enter the Sentense:- ")

length=len(Sentence)
Total_Character=len(Sentence.replace(" ",""))
Total_Words=len(Sentence.split())
Total_Space=(Sentence.count(" "))
Uppercase=Sentence.upper()
Lowercase=Sentence.lower()


vowels = "aeiouAEIOU"
vowel_count = 0
for char in Sentence:
    if char in vowels:
        vowel_count += 1


consonant_count = 0
for char in Sentence:
    if char.isalpha() and char not in vowels:
        consonant_count += 1


digit=0
for char in Sentence:
    if char.isdigit():
        digit+=1


special_character_count = 0
for char in Sentence:
    if not char.isalpha() and not char.isdigit() and char != " ":
        special_character_count += 1


print("\n---------- Word Count result ----------")
print("Total lenght of Sentense:- ",length)
print("Total Characters(wihtout Spaces):- ",Total_Character)
print("Total Words:- ",Total_Words)
print("Total Space:- ",Total_Space)
print("Total Vowels:- ",vowel_count)
print("Total Consonants:- ", consonant_count)
print("Total Digits:- ",digit)
print("Total Special Characters:-", special_character_count)
print("Sentense in Uppercase:- ",Uppercase)
print("Sentense in Lowercase:- ",Lowercase)