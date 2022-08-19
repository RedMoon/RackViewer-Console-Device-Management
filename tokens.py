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