"""
A random HELLOWORLD
"""
from random import randint

greetings = ['Hello World' , 'Hola Mundo' , 'Ciao Mondo' , 'Bonjour le Monde', 'Hallo Welt']
value = randint(0,4)
line='-'
greeting = greetings[value]
print(line.strip() * len(greeting))
print(greeting)
print(line.strip() * len(greeting))
