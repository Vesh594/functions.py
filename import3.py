print("Let's import an entire module: ")
import functions3
functions3.make_pizza(16, 'pepperoni')
functions3.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\nLet's import specific functions:")
from functions3 import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\nLet's use as to give a function on alias")
# Alias - an alternate nickname to a function (ex:mp)
from functions3 import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\nLet's use as to give a module an alias: ")
import functions3 as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\nLet's import all functions in a module: ")
# To import every function, use *
from functions3 import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\nLet's print models: ")
import functions3
functions3.print_models('cardboard', 'black', 'yellow', 'red')
from functions3 import print_models
print_models('cardboard', 'black', 'yellow', 'red')
from functions3 import print_models as pm
pm('cardboard', 'black', 'yellow', 'red')
import functions3 as f3
f3.make_print_models('cardboard', 'black', 'yellow', 'red')
from functions3 import *
print_models('cardboard', 'black', 'yellow', 'red')

