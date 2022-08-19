from ast import arg
from posixpath import split
import sys  # Импортируем библиотеку sys
import os  # Импортируем библиотеку os
class variable:
    variables = {"version": 1.0}
    
class Tokens:
    main = ["sum","delete","var","$"]
    def func_factory(operation,args):
        if operation == 'sum':
            def summ():
                return sum([int(item) for item in args])
            return summ
        elif operation == 'var':
            def mul():
                if(args[1] == "="):
                    variable.variables[args[0]] = args[2]
                    return variable.variables[args[0]]
                else: return "error = is unexpected"
            return mul
        elif operation == '$':
            def mul():
               return variable.variables[args[0]]
            return mul
        else:
            raise Exception

class Lexer:
    def parse( vars):
        if Tokens.main.__contains__(vars[0]):
            func = Tokens.func_factory(vars[0],args=vars[1:])
            print(func())
print("Welcome to the Rackviewer Console Device Management RVC")
while(True):
    value = input("->")
    Lexer.parse(value.split(" "))