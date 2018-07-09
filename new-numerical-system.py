import string


def new_numeral_system(number):
    ind = string.ascii_uppercase.find(number)
    return [string.ascii_uppercase[x] + " + " + string.ascii_uppercase[y] for x in range(0, ind/2) for y in range(ind, ind/2 , -1)]

print new_numeral_system("C")
print new_numeral_system("B")