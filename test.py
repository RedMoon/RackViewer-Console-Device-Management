from ast import arg
from logging import exception
from posixpath import split
import os  # Импортируем библиотеку os
from termcolor import colored, cprint


class variable:
    variables = {"version": 1.0}

# command -add "restartGUI" "systemctl restart %%"


class Tokens:
    main = ["sum", "delete", "var", "$", "service", "execute","command"]

    def func_factory(operation, args):
        if operation == 'sum':
            def summ():
                return sum([int(item) for item in args])
            return summ
        elif operation == 'var':
            def mul():
                if (args[1] == "="):
                    variable.variables[args[0]] = args[2]
                    return variable.variables[args[0]]
                else:
                    return "error = is unexpected"
            return mul
        elif operation == '$':
            def mul():
                return variable.variables[args[0]]
            return mul
        elif operation == 'command':
            def mul():
                if (args[0] == "-add"):
                    f = open('customCommands.txt','a')
                    name = str(args[1]).replace("\"" ,"")
                    action = ""
                    for i in range(2,len(args)):
                        action += f" {args[i]}"
                    #action = str(action).replace("\"" ,"")
                    print(args[2])
                    f.write(f"{name}:{action}\r\n") 
                    f.close()
                return f"command named {name} with action {action} was created!"
            return mul
        elif operation == 'execute':
            f = open('customCommands.txt', 'r')
            for line in f.readlines():
                if (args[0] == line.split(":")[0]):
                    command = line.split(":")[1]
                    for i in range(len(args)):
                        if (i == 0):
                            i += 1
                        command = command.replace(f"%{i}%", args[i])
                    os.system(command)
            f.close()
        elif operation == 'service':
            params = {"-s": "start", "-k": "kill", "-r": "restart"}

            def mul():
                output = ""
                for param in params:
                    if (param == args[0]):
                        output = params[param] + " procces " + args[1]
                return output
            return mul
        else:
            raise exception


class Lexer:
    def parse(vars):
        if Tokens.main.__contains__(vars[0]):
            func = Tokens.func_factory(vars[0], args=vars[1:])
            print(func())
welcome = colored(
    'Welcome to the Rackviewer Console Device Management RVC 127.0.0.1 connected', 'red', attrs=['blink'])
print(welcome)
while (True):
    try:
        value = input("->")
        Lexer.parse(value.split(" "))
    except:
        pass
