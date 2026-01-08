# keyword def informs python that you're defining a function
def greet_user():
    """Display a simple greeting."""
    # docstring describes what the function does
    print("Hello!")
greet_user()
# What comes after def tells what kind of information the function needs to do its job
# You have to call your function at the end
print("\nLet's pass information to a function:\n")
def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")
greet_user('jesse')
print("\nWhat I learned today?\n")
def display_message():
    print("I learned about functions in this chapter.")
display_message()
print("\nWhat is my favorite book?\n")
def favorite_book(title):
    print(f"My favorite book is {title.title()}.")
favorite_book('Rich dad, poor dad')
print("\nPositional arguments:\n")
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
print("\nMultiple function calls:\n")
describe_pet('dog', 'willie')
print("\nOrder matters in positional arguments\n")
print("Keyword Arguments:")
describe_pet(animal_type = 'hamster', pet_name = 'harry')
print("\nDefault Values:\n")
def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
print("Let's do T-Shirts")
def make_shirt(size, message):
    # Positional arguments
    print(f"The shirt size is {size} and the message printed on it is: '{message}'")
make_shirt("S", "Fuck you")
# Keyword arguments
def make_shirt(size = 'S', message = 'fuck you'):
    print(f"The shirt size is {size} and the message printed on it is: '{message.title()}'")
make_shirt()
print("\nLet's do large shirts:\n")
def make_shirt(size, message):
    print(f"The shirt size is {size.title()} and the message printed on it is: '{message.title()}'")
default_message = 'i love python'
make_shirt('large', default_message)
make_shirt('medium', default_message)
make_shirt('small', 'i love javascript')
print("\nLet's do cities:\n")
def describe_city(city_name, country):
    print(f"{city_name.title()} is in {country.title()}.")
default_value = 'Malaysia'
describe_city('kuala lumpur', default_value)
describe_city('seremban', default_value)
describe_city('prague', 'czechia')
print("\nLet's return a simple value:\n")
# Return a full name variable to a musician variable
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("\nLet's make an argument optional:\n")
def get_formatted_name(first_name, last_name, middle_name=''):
    #The optional variable with an empty string and at last
    #position will be ignored unless the user provides a value
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("\nLet's return a dictionary:\n")
def build_person(first_name, last_name):
    person = {'first': first_name, 'last':last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
# store a person's age
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)
print("\nLet's use a function with a while loop:\n")
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:\n")
    print("(Enter 'quit' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name: ")
    if l_name == 'quit':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
print("\nLet's do city names to practice:\n")
def city_country(city, country):
    place = {city, country}
    return place.title()
first = city_country("Santigo", "Chile")
print(first)
second = city_country("prague", "czechia")
print(second)
third = city_country("seremban", "malaysia")
print(third)
print("\nLet's do albums:\n")
def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist, 'title': title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album.title()
taylor = make_album('Taylor Swift', 'Wannabe', number_of_songs=67)
print(taylor)
elon = make_album('elon musk', 'rich', number_of_songs=69)
print(elon)
vesh = make_album('vesh', 'hana', number_of_songs=9)
print(vesh)
print("\nLet's do user albums:\n")
def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist, 'title': title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album.title()
while True:
    print("\nPlease give me info about your favorite artist:")
    print("(Enter 'quit' at any time to quit)")
    artist = input("Artist name: ")
    if artist == 'quit':
        break
    title = input(f"Favorite album from {artist.title()}: ")
    if title == 'quit':
        break
    number_of_songs = input("How many song? ")
    if number_of_songs == 'quit':
        break
    user_album = make_album(artist, title, number_of_songs)
    print(f"\nHello, {user_album}!")
    print(f"\n My favorite artist is {artist.title()} and my favorite album from them is {title.title()} with {number_of_songs}.")
