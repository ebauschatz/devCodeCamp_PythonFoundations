#Task 1
#Steps to solve:
#create a variable to store the users's number
#create a variable to keep track of the number as it changes
#create a variable to track if we have looped back to the original number
#iterate over each character in the number as long as we haven't reached 1 or looped back around
#   translate the character to an integer
#   square it, and add it to the running total
#   compare the original number to the new number (as a string)
#       if they match, break out
#       if the don't, set the number to the new value and keep looping
#print the result based on if we looped back around or not
original_number = input('Please enter a number: ')
number = original_number
returned_to_original_number = False

while number != '1' and returned_to_original_number is False:
    new_number_value = 0
    for char in number:
        digit = int(char)
        new_number_value += digit ** 2
    number = str(new_number_value)
    if number == original_number:
        returned_to_original_number = True

if returned_to_original_number is True:
    print(f'{original_number} is not a happy number')
else:
    print(f'{original_number} is a happy number')


#Task 2
#iterate through numbers beween 1 and 100
#   iterate through numbers between 2 and the current number from above
#   if the two numbers divide evenly, move on to the next top number
#   otherwise print the number
neither_prime_nor_composite = [0, 1]

for number in range(1, 101):
    divisor_found = False
    for divisor in range(2, number):
        if number % divisor == 0:
            divisor_found = True
            break
    if divisor_found is True:
        continue
    if number not in neither_prime_nor_composite:
        print(number)


#Task 3
#Steps to solve:
#create a variable to store user input for a starting number
#if nothing is entered, start at 1
#create a variable to store  how many numbers in the sequence to return
#create variables to track the previous two numbers in the sequence
#for the requested number of return numbers:
#   print the current number in the series
#   shift the variables down to reflect the iteration
#   set the current number to the sum of the previous two
starting_number_input = input('Please enter a starting number or leave blank to start at 1: ')
number_of_iterations_input = input('Please enter how many numbers in the sequence to return: ')
number_of_iterations = int(number_of_iterations_input)

if starting_number_input == '':
    current_number = 1
else:
    current_number = int(starting_number_input)

previous_number = 0
before_previous_number = 0

for counter in range(number_of_iterations):
    print(current_number)
    before_previous_number = previous_number
    previous_number = current_number
    current_number = before_previous_number + previous_number