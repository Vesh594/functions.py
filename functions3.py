print("Let's import an entire module: ")
def make_pizza(size, *toppings):
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(topping)
print("\nLet's style functions:")
# if you specify a default value for a parameter, no 
# spaces used on either side of the equal sign:
def function_name(parameter_0, parameter_1='default value'):
# The same convention should be used for keyword arguments in function calls:
  function_name(parameter_0='baby', parameter_1='value')
def function_name(
    parameter_0, parameter_1, parameter_2,
    parameter_3, parameter_4, parameter_5):
  function_name('baby')
print("\nLet's print models: ")
def print_models(materials, *colors):
  print("The model made out of {materials} in the following colors:")
  for material in materials:
    print(material)
