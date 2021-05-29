string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count_vowels = 0

for char in string:
    count_vowels += 1 if char in vowels else 0

print(count_vowels)
