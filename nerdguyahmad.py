'''
Weekly Challenge #6

Discord username: nerdguyahmad#3195
'''
def swapcase(string):
    chars = [char for char in string]
    new = []
    for char in chars:
        if char.lower() == char:
            new.append(char.upper())
        elif char.upper() == char:
            new.append(char.lower())
        else:
            new.append(new)
    return ''.join(new)

print(swapcase('HeLLo wORLd'))
