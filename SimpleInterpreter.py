def interpret(value, commands, args):
    coms = {'+': lambda a,b : a+b, '-': lambda a,b : a-b, '*': lambda a,b : a*b}

    for c, a in zip(commands, args):
        value = coms[c](value, a)
    return value

print interpret(1, ["+"],[2])
print interpret(1, ['+', '*','+'], [1, 3, 5])
print interpret(4, ['-'], [2])