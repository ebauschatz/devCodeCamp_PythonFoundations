import math

#Tasks from https://docs.google.com/document/d/1oGhlkKPPzlTo6J7e1CbRnSGHMbEFrvE4/edit

#Task 1
#https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
year_input = input('Please enter a year to begin calculating after: ')
year = int(year_input)
max_years_to_return_input = input('Please enter the number of following leap years to return: ')
max_years_to_return = int(max_years_to_return_input)

year_count = 0

while year_count < max_years_to_return:
    year += 1
    if year % 4 != 0:
        continue
    if year % 100 == 0 and year % 400 != 0:
        continue
    print(year)
    year_count += 1


#Task 2
def validate_palindrome_status(test_string):
    forwards_index = 0
    backwards_index = len(test_string) - 1
    palindrome_invalidated = False

    while palindrome_invalidated is False:
        if test_string[forwards_index] != test_string[backwards_index]:
            palindrome_invalidated = True
            break
        forwards_index += 1
        backwards_index -= 1
        if forwards_index >= backwards_index:
            break
    
    if palindrome_invalidated is True:
        return False
    else: 
        return True

user_string = input('Please input any string: ')
user_string_length = len(user_string)
longest_substring_length = 0

for substring_start_index in range(user_string_length):
    if user_string_length - substring_start_index <= longest_substring_length:
        break
    for substring_end_index in range(user_string_length, substring_start_index + 1, -1):
        if substring_end_index - substring_start_index <= longest_substring_length:
            break
        substring = user_string[substring_start_index : substring_end_index]
        substring_is_palindrome = validate_palindrome_status(substring)
        if substring_is_palindrome is True:
            longest_substring_length = len(substring)
            break
print(longest_substring_length)


#Task 3
seconds_input = input('Please enter a number of seconds: ')
seconds = int(seconds_input)
seconds_in_minute = 60
minutes_in_hour = 60

all_minutes = math.floor(seconds / seconds_in_minute)
seconds_reminder = seconds % seconds_in_minute
hours = math.floor(all_minutes / minutes_in_hour)
minutes_remainder = all_minutes % minutes_in_hour

print(f'Hours: {hours}')
print(f'Minutes: {minutes_remainder}')
print(f'Seconds: {seconds_reminder}')


#Task 4
number_input = input('Please enter an integer: ')
number = int(number_input)
comparison_number = 13

difference = abs(comparison_number - number)
if number > comparison_number:
    difference *= 2

print(f'The difference (or doubled difference) is {difference}')


#Task 5
first_number = input('Please enter the first number: ')
second_number = input('Please enter the second number: ')
third_number = input('Please enter the third number: ')
match_found = False
numbers = [first_number, second_number, third_number]

for index, number in enumerate(numbers):
    last_character = number[-1]
    for subindex in range(index + 1, len(numbers)):
        other_character = numbers[subindex][-1]
        if last_character == other_character:
            match_found = True
            break
    if match_found:
        break

print(match_found)


#Task 6
string_input = input('Please enter a string: ')
characters_to_find = ['a', 'b']
separation = 3
sequence_found = False

for index in range(len(string_input) - separation):
    char = string_input[index]
    if char not in characters_to_find:
        continue
    separated_character = string_input[index + separation]
    if separated_character in characters_to_find and separated_character != char:
        sequence_found = True
        break
print(f'Characters with desired separation found: {sequence_found}')


#Task 7
input_text = input('Please enter any string: ')
character_counts = {'p': 0, 't': 0}

for char in input_text:
    if char in character_counts:
        character_counts[char] += 1
for char in character_counts:
    print(f'{char}: {character_counts[char]}')

#Task 8
input_text = input('Please enter any string: ')
total = 0

for char in input_text:
    if char.isdigit() is True:
        total += int(char)
print(f'The sum of digits from the string is: {total}')


#Task 8
fraction_input = input('Please enter a fraction: ')
division_char_index = fraction_input.find('/')
numerator = fraction_input[0 : division_char_index]
denominator = fraction_input[division_char_index + 1 : len(fraction_input)]

if int(numerator) > 0 and int(denominator) > 0 and numerator < denominator:
    print('This is a proper fraction')
else:
    print('This fraction is improper')


#Task 10
def translate_to_pig_latin(english_word):
    return english_word[1 : len(english_word)] + english_word[0:1] + 'ay'

def translate_from_pig_latin(pig_latin_word):
    word_length = len(pig_latin_word)
    return pig_latin_word[word_length - 3 : word_length - 2] + pig_latin_word[0 : word_length - 3]

original_string = input('Please enter a string of multiple words: ')
original_string_words = list(original_string.split(' '))
pig_latin_words = []
back_translated_words = []

for word in original_string_words:
    translated_word = translate_to_pig_latin(word)
    pig_latin_words.append(translated_word)

for word in pig_latin_words:
    back_translated_word = translate_from_pig_latin(word)
    back_translated_words.append(back_translated_word)

pig_latin_string = ' '.join(pig_latin_words)
print(f'Pig Latin translation: {pig_latin_string}')
back_translated_string = ' '.join(back_translated_words)
print(f'Back translation from Pig Latin: {back_translated_string}')


#Task 11
rotations_input = input('Enter a number of positions to rotate the list by: ')
rotations = int(rotations_input)
number_list = [1, 2, 3, 4, 5, 6]
#Avoid unnecessary rollover
rotations_to_original_position = len(number_list)
rotations = rotations % rotations_to_original_position

for rotation_counter in range(rotations):
    first_element = number_list.pop(0)
    number_list.append(first_element)

print(number_list)