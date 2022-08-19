from posixpath import split
import sys  # Импортируем библиотеку sys
import os  # Импортируем библиотеку os

class Tokens:
    main = ["create","delete"]
    def func_factory(operation):
        if operation == 'create':
            def summ(a, b):
                return a + b
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
            func = Tokens.func_factory(vars[0])
            print(func(1,2))
print("Welcome to the Rockviewer Console Device Management RVC")
value = input("->")
Lexer.parse(value.split(" "))
