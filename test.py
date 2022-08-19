from ast import arg
from posixpath import split
import sys  # Импортируем библиотеку sys
import os  # Импортируем библиотеку os

class Tokens:
    main = ["sum","delete"]
    def func_factory(operation,args):
        if operation == 'sum':
            def summ():
                return int(args[0]) + int(args[1])
            return summ
        elif operation == 'delete':
            def mul(a, b):
                return a * b
            return mul
        else:
            raise Exception

class Lexer:
    def parse( vars):
        if Tokens.main.__contains__(vars[0]):
            func = Tokens.func_factory(vars[0],args=[vars[1],vars[2]])
            print(func())
print("Welcome to the Rockviewer Console Device Management RVC")
while(True):
    value = input("->")
    Lexer.parse(value.split(" "))