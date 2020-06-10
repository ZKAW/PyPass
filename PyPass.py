from random import choice as rand
from string import ascii_letters, digits
specials = "#~!/?%°@&-_{}[]()*$."

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


def randPass(stringLength, isNumber, isSpecial):
    if isNumber and isSpecial == True:
        asciMap = ascii_letters + digits + specials
    elif isNumber == True:
        asciMap = ascii_letters + digits
    elif isSpecial == True:
        asciMap = ascii_letters + specials
    else:
        asciMap = ascii_letters
    return ''.join(rand(asciMap) for i in range(stringLength))


print("\nYour password is: "+randPass(passLength, isNumber, isSpecial))