#Task 1
#Steps to solve:
#   create a variable to hold the user input
#   create an empty string to eventually hold the reversed string
#   iterate backwards through the input string and append each character to the "reversed" string
#   print the reversed string

user_string = input('Please enter any string: ')
reversed_string = ''

for index in range(len(user_string) - 1, -1, -1):
    reversed_string += user_string[index]
print(reversed_string)


#Task 2
#Steps to solve:
#   create a variable to hold the user input
#   create a variable to hold the edited string
#   iterate through the user input string
#       if this character is a space, set a variable to reflect that, add the space to the edited string, and move on to the next iteration
#       if the previous character was a space or this is the very first character, replace this character in the string with it's upper case version
#       otherwise add this character to the new string with no edits
#   print the result

user_string = input('Please enter any string: ')
edited_string = ''

space_found = False
for index in range(len(user_string)):
    if user_string[index] == ' ':
        space_found = True
        edited_string += user_string[index]
        continue
    if space_found or index == 0:
        edited_string += user_string[index].upper()
        space_found = False
    else:
        edited_string += user_string[index]
print(edited_string)


#Task 3
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


#Task 4
#Steps to solve:
#   create a string to hold the user input
#   create a string to hold the compressed version
#   create a character count variable
#   create a previous character variable
#   iterate through the string
#       if this character is the same as the previous existing character, increment the counter
#         if this is also the last character in the string, append the counter and character
#       otherwise append the counter and previous character to the compressed string, 
#           reset the counter, and change the previous character variable
#   print the results

user_string = input('Please enter any string: ')

compressed_string = ''
character_count = 0
previous_character = ''
end_of_string = len(user_string) - 1

for index, char in enumerate(user_string):
    if char == previous_character:
        character_count += 1
        if index == end_of_string:
            compressed_string += str(character_count) + char
        continue
    if index > 0:
        compressed_string += str(character_count) + previous_character
    character_count = 1
    previous_character = char
    if index == end_of_string:
            compressed_string += str(character_count) + char

print(compressed_string)