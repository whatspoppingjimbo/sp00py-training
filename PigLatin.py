# transfer initial consonant(s) to end of word
# add ay to the end of that word
# for words that begin with vowels add way to end

word = input("Enter a word ")
vowels = ['a', 'e', 'i', 'o', 'u']
if word[0] is "a" or word[0] is "e" or word[0] is "i" or word[0] is "o" or word[0] is "u":
    word = + "way"
else:
    word = word[1:] + word[0] + "ay"

print(word)
