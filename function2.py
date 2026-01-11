print("Let's pass a list:")
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print("\nLet's modify a list in a function:\n")
def print_models(unprinted_designs, completed_models):
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)

# Prepare lists and call the functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print("\nLet's prevent a function from modifying a list:\n")
# The slice notation [:] makes a copy of the list to send to the function
print_models(unprinted_designs[:], completed_models)
a = [1, 2, 3, 4]
b = a[:]
b == a 
# OR
b is a
b.append(5)
print(a)
print(b)
print("\nLet's do messages:")
def show_messages(messages):
  for message in messages:
     print(message)
messages = ['Hey', 'I love you', 'Take care']
show_messages(messages)
print("\nLet's send messages:\n")
def send_messages(unsent_messages, sent_messages):
   while unsent_messages:
    saved_messages = unsent_messages.pop()
    print(f"Sending message: {saved_messages}")
    sent_messages.append(saved_messages)
def show_messages(sent_messages):
   print("\nThe following messages have been sent: ")
   for sent_message in sent_messages:
    print(sent_message)
unsent_messages = ['Hey', 'I love you', 'Take care']
sent_messages = []
send_messages(unsent_messages, sent_messages)
show_messages(sent_messages)
print("\nLet's pass an arbitrary number of arguments:")
def make_pizza(*toppings):
  print("Making a pizza with the following toppings:")
  for topping in toppings:
   print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# * tells Python to make a tuple called topping containing all
# the values this function receives
print("\nLet's mix positional and arbitrary arguments:")
def make_pizza(size, *toppings):
  print(f"Making a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# This makes sure the list in toppings will not change
print("\nLet's use arbitrary keyword arguments:")
def build_profile(first, last, **user_info):
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info
user_profile = build_profile('albert', 'einstein', 
                             location = 'princeton',
                             field = 'physics')
print(user_profile)
print("\nLet's do sandwiches:")
def sandwich_ingredients(*ingredients):
  print("Making a sandwich with the following ingredients: ")
  for ingredient in ingredients:
     print(f"- ingredients")
sandwich_ingredients('chicken')
sandwich_ingredients('tuna')
sandwich_ingredients('egg')
print("\nLet's do user profile: ")
def build_profile(first, last, **user_info):
  user_info['first name'] = first
  user_info['last name'] = last
  return user_info
user_profile = build_profile('veshnavi', 'mahendran', 
                             philosophical_view = 'nihillist',
                             religious_view = 'atheist',
                             sexuality = 'lesbian')
print(user_profile)
print("\nLet's do cars: ")
def cars(manufacturer, model, **car_info):
  car_info['Manufacturer'] = manufacturer
  car_info['Car Model'] = model
  return car_info
buy_car = cars('einstein', 'tesla', color='black', 
               price='$100000')
print(buy_car)
