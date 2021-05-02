"""
A random HELLOWORLD
"""

from colorama import *
from random import randint

# colorama initialise
init()

greetings = ['Hello World    .' , 'Hola Mundo     .' , 'Ciao Mondo     .' , 'Bonjour le Monde', 'Hallo Welt     .']
value = randint(0,4)
line='-'
greeting = greetings[value]
linex = line.strip() * len(greeting)

print(Cursor.POS(5,5)+ linex)
print(Fore.BLUE +
          Back.LIGHTYELLOW_EX +
          Cursor.POS(5, 6) + # (col,row)
          greeting +
          Style.RESET_ALL)
print(Cursor.POS(5,7)+linex)
