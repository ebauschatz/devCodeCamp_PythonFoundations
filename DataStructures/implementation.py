#TASK 1.1
from distutils.command.config import config


def configure_months():
    """Create an ordered tuple of the months of the Gregorian calendar

    Returns:
        Tuple of all months in order from January - December
    """
    return ('January', 'February', 'March', 'April', 'May',
     'June', 'July', 'August', 'September', 'October', 'November', 'December')

def find_month_from_float(number):
    """Given a float between 1.0 and 12.99*, return the month that corresponds to the whole number portion
    of the float without rounding

    Args:
        number: float
            a float to find the month from

    Effects:
        Prints the resulting month to the console
    """
    months = configure_months()
    target_month = months[int(number) - 1]
    print(f'The resulting month is: {target_month}')


#TASK 1.2
def configure_initial_foods():
    """Creates a set of five fruits and vegetables

    Returns:
        A set of strings representing fruits or vegetables
    """
    return {'apple', 'pear', 'celery', 'pea', 'lima bean'}

def add_favorite_food(food, foods):
    """Adds a new favorite food to an existing set of foods

    Args:
        food: string
            the new food to add to the set
        foods: set
            the existing list of favorite foods

    Effects:
        The new food will be added to the existing set
    """
    foods.add(food)

def display_all_foods(foods):
    """Displays all foods from a set to the console

    Args:
        foods: set
            a set of all foods to display

    Effects:
        All foods from the set will be displayed to the console
    """
    print('\nThe following foods are currently in the foods set:')
    for food in foods:
        print(food)

def favorite_fruits_and_veggies_configuration(new_foods):
    """Overall function to add new foods to the standard list and print the results

    Args:
        new_foods: list(string)
            a list of strings representing new fruits or vegetables to add to the list

    Effects:
        The default list of fruits and vegetables and new additions will be printed to the console
    """
    foods = configure_initial_foods()
    for food in new_foods:
        add_favorite_food(food, foods)
    display_all_foods(foods)


#TASK 1.3
def get_user_information():
    """Returns hard-coded user profile information

    Returns:
        A dictionary for the user containing personal information
    """
    return {
        'first_name': 'Luna',
        'last_name': 'Lovegood',
        'email_address': 'nargles@quibbler.uk',
        'phone_number': '555-555-1234'
    }

def display_user_information():
    """Displays formatted user profile information to the console

    Effects:
        Displays user first/last name, email, and phone number
    """
    user_information = get_user_information()
    print(f'''\nBelow is the user\'s information:
    First Name: {user_information['first_name']}
    Last Name: {user_information['last_name']}
    Email Address: {user_information['email_address']}
    Phone Number: {user_information['phone_number']}''')


##TASK 2
def configure_family_members():
    """Creates a preset list of immediate family members

    Returns:
        A list of dictionaries, where each dictionary repensents a family member
    """
    return [
        {
            'first_name': 'Andrew',
            'last_name': 'English',
            'relation': 'father'
        },
        {
            'first_name': 'Diane',
            'last_name': 'English',
            'relation': 'mother'
        },
        {
            'first_name': 'Kat',
            'last_name': 'English',
            'relation': 'sister'
        }
    ]

def display_family_relations():
    """Displays immediate family members' first names and relation

    Effects:
        Displays family information to the console
    """
    family_members = configure_family_members()
    print('Immediate family members:')
    for family_member in family_members:
        print(f'\t{family_member["first_name"]} is my {family_member["relation"]}')