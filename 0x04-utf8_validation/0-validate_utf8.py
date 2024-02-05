#!/usr/bin/python3
''' UTF-8 Validation '''


def validUTF8(data):
    ''' vald utf-8 '''

    i = 0
    while i < len(data):
        if 0 <= data[i] < 128:
            i += 1
        elif data[i] > 128:
            if bin(data[i])[2:].startswith('10'):
                i += 1
            elif bin(data[i])[2:].startswith('110'):
                if not bin(data[i + 1])[2:].startswith('10'):
                    return False
                i += 2
            elif bin(data[i])[2:].startswith('1110'):
                stop = i + 2
                while i <= stop:
                    if not bin(data[i + 1])[2:].startswith('10'):
                        return False
                    i += 1
            elif bin(data[i])[2:].startswith('11110'):
                stop = i + 3
                while i <= stop:
                    if not bin(data[i + 1])[2:].startswith('10'):
                        return False
                    i += 1
            else:
                return False
        else:
            return False
    return True
