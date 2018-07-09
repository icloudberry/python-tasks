# Write a simple interpreter which understands "+", "-", and "*" operations.
# Apply the operations in order using command/arg pairs starting with the initial value of `value`.
# If you encounter an unknown command, return -1.
#
#
# interpret(1, ['+'], [1]) -> 2
# interpret(4, ['-'], [2]) -> 2
# interpret(1, ['+', '*'], [1, 3]) -> 6

def interpret(value, commands, args):
    coms = {'+': lambda a,b : a+b, '-': lambda a,b : a-b, '*': lambda a,b : a*b}

    for c, a in zip(commands, args):
        if c in coms:
            value = coms[c](value, a)
        else:
            return -1
    return value

print interpret(1, ["+"],[2])
print interpret(1, ['+', '*','+'], [1, 3, 5])
print interpret(4, ['-'], [2])
print interpret(4, ['-',':'], [2, 1])