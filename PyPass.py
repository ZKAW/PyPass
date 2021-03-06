# coding: cp1252

from random import choice as rand
from string import ascii_letters, digits
specials = "#~!/?%°@&=-_{}[]()*$." # Here you can change the default special characters map

try:
    input = raw_input # if python version <= 2.7, set input pour raw_input
except NameError:
    pass # else, don't change anything

try:
    passLength = int(input("Password length ([default = 12]): "))
except ValueError:
    passLength = 12

includeNumber = input("Include numbers ? (O/n): ")
includeSpecial = input("Inclure special characters ? (O/n): ")

if "n" in includeNumber:
    isNumber = False
else:
    isNumber = True
if "n" in includeSpecial:
    isSpecial = False
else:
    isSpecial = True


def randPass(stringLength=12, isNumber=True, isSpecial=True, specialChars=specials):
    try:
        specialChars = specialChars.decode('utf8')
    except:
        pass

    if isNumber and isSpecial == True:
        asciMap = ascii_letters + digits + specialChars
    elif isNumber == True:
        asciMap = ascii_letters + digits
    elif isSpecial == True:
        asciMap = ascii_letters + specialChars
    else:
        asciMap = ascii_letters
    return ''.join(rand(asciMap) for i in range(stringLength))


print("\nYour password is: "+randPass(passLength, isNumber, isSpecial))
# print("\nYour password is: "+randPass(passLength, isNumber, isSpecial, '#&$%=~'))
"""You can change the special charMap by adding a fourth argument to the randPass() function"""