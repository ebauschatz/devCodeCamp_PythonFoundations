import re
import string
import math

#Task 1
#Steps to solve
#create a variable to store the target number and convert it to an int
#set up the integer list
#iterate through the list
#   if the current element is greater than the target, the sum won't work so keep going
#   iterate through the elements farther down the list
#       if any sum of the current element and an element farther down matches the sum, record both indexes and stop
target_number_input = input('Please enter a target number: ')
target_number = int(target_number_input)

integer_array = [5, 17, 77, 50]
index_pair = []

for index, number in enumerate(integer_array):
    if number > target_number:
        continue
    for subindex in range(index + 1, len(integer_array)):
        if number + integer_array[subindex] == target_number:
            index_pair = [index, subindex]
            break
    if index_pair != []:
        print(index_pair)
        break

#Task 2
#Steps to solve:
#   create a variable to hold the user input
#   create variables to hold a "from the front" index tracker and a "from the back" index tracker
#   iterate through the string until the "front" and "back" index trackers meet or overlap
#       compare the character in the current "front" index to the corresponding "back" character
#       if they do not match, the word is not a palindrome, set a boolean to reflect this and break out of the loop
#       otherwise, step the "front" and "back" counters closer to each other
#       if the "front" and "back" index trackers meet or overlap, the entire word has been checked

user_string = input('Please input any string: ')

forwards_index = 0
backwards_index = len(user_string) - 1
palindrome_invalidated = False

while palindrome_invalidated is False:
    if user_string[forwards_index] != user_string[backwards_index]:
        palindrome_invalidated = True
        break
    forwards_index += 1
    backwards_index -= 1
    if forwards_index >= backwards_index:
        break

if palindrome_invalidated is True:
    print(f'\'{user_string}\' is not a valid palindrome')
else:
    print(f'\'{user_string}\' is a valid palindrome')


#Task 3
#Steps to solve
#set up the list of integers
#sort the list
#iterate over the list
#   if the current number and the previous number are not adjacent, the list is not sequential
#if the loop completes without finding any non-sequential elements, the list is sequential
integer_list = [17, 15, 20, 19, 21, 16, 18]
integer_list.sort()
can_be_sequenced = True

for index in range(1, len(integer_list)):
    if integer_list[index] - 1 != integer_list[index - 1]:
        can_be_sequenced = False
        break
print(can_be_sequenced)


#Task 4
#Steps to solve
#create variables to hold count for positve and negative numbers
#iterate over the list
#   if the number is greater than zero increment the positive counter
#   if the number is less than zero increment the negative counter
integer_list = [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]
count_of_positive_numbers = 0
count_of_negative_numbers = 0

for number in integer_list:
    if number > 0:
        count_of_positive_numbers += 1
    elif number < 0:
        count_of_negative_numbers += 1

print([count_of_positive_numbers, count_of_negative_numbers])


#Task 5
#Steps to solve
#create a variable for the user input
#split the string into a list at each space character
#convert the list of strings into a list of integers
#sort the list ascending
#find the first (smallest) and last (largeset) elements of the list
#concatenate them into a space-delimited string
number_string = input('Please enter a space-delimited string of numbers: ')
number_list = number_string.split(' ')
for index, number in enumerate(number_list):
    number_list[index] = int(number)
number_list.sort()
number_minmax_string = str(number_list[0]) + ' ' + str(number_list[-1])
print(number_minmax_string)


#Task 6
#Steps to solve
#create a variable for the input email address
#pattern match the entire string to ensure that it contains in order:
#   - at least one but no more than 64 letters, numbers or characters period, dash, underscore
#   - the @ symbol
#   - at least one of letters, numbers or characters period, dash, underscore
#   - a period
#   - at least two but no more than six letters or numbers
#if a match was not found, return invalid message
#otherwise return success message
# https://docs.python.org/3/library/re.html
email_input = input('Please enter an email address to validate: ')
match = re.fullmatch('[A-z0-9.\-_]{1,64}@[A-z0-9.\-_]+\.[A-z0-9]{2,6}', email_input)
if match is None:
    print(f'The email {email_input} is invalid')
else:
    print(f'The email {email_input} is valid')

#Task 7
#Steps to solve
#create a variable to store the input string
#create a list of lowercase characters
#create a list of corresponding numbers (in order with the character list above)
#combine the lists into key-value pairs where the letter is the key and the number is the value
#for each character in the string
#   if it exists as a key in the cross-reference, add the corresponding value to a new list
#convert the mapped list to a space-delimited string
#print the string
# https://docs.python.org/3/library/string.html
# https://www.w3schools.com/python/ref_func_zip.asp
# https://www.w3schools.com/python/ref_string_join.asp
input_string = input('Please enter any lowercase alphabetic string: ')
mapped_list = []

characters = list(string.ascii_lowercase)
numbers = list(range(1, 27))
cross_reference = dict(zip(characters, numbers))

for char in input_string:
    if char in cross_reference:
        mapped_list.append(str(cross_reference[char]))

mapped_string = ' '.join(mapped_list)
print(mapped_string)


#Task 8
#Steps to solve:
#create a variable to store the input of the current lock position
#create a variable to store the target lock position
#for each dial
#   find the current and targer positions
#   find how far apart the positions are
#   add that distance to the running total
current_combination = input('Please enter the lock\'s current position: ')
target_combination = input('Please enter the lock\'s desired combination: ')
total_turns = 0
low_rollover_position = 0
high_rollover_position = 9
max_turns = math.ceil((high_rollover_position - low_rollover_position) / 2)

for dial_index in range(len(current_combination)):
    current_position = int(current_combination[dial_index])
    target_position = int(target_combination[dial_index])
    if current_position == target_position:
        continue
    else:
        direct_turns = abs(current_position - target_position)
        if direct_turns > max_turns:
            positions = [current_position, target_position]
            positions.sort()
            rollover_turns = abs(low_rollover_position - positions[0]) + abs(high_rollover_position - positions[1]) + 1
            total_turns += rollover_turns
        else:
            total_turns += direct_turns

print(f'{total_turns} turn(s) are required to adjust the lock to the desired combination')


#Task 9
#Steps to solve:
#create a variable to store the user input integer
#loop backwards through the input and create a reversed string
#convert the reversed string to an integer
#take the reciprocal of the integer
number_input = input('Please enter a positive integer: ')
number_input_reverse = ''

for index in range(len(number_input) - 1, -1, -1):
    number_input_reverse += number_input[index]
number_reciprocal = int(number_input_reverse)
number_reverse_reciprocal = 1 / number_reciprocal

print(number_reverse_reciprocal)