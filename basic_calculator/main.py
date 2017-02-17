"""This is the entry point of the program."""


def basic_calculator(num_1, num_2, oper):
    if oper == 'add':
        return num_1 + num_2
    elif oper == 'subtract':
        return num_1 - num_2
    elif oper == 'multiply':
        return num_1 * num_2
    elif oper == 'divide':
        if num_2 == 0:
            return 'Does not exist'
        else:
            return num_1 / num_2
    else:
        return 'Invalid operation'