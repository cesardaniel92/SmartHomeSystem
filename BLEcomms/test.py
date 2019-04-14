from binascii import hexlify

test = 0x0e

def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result



# allHex = hexlify(line)
#
# humHex =
# humHex = humHex >> 16
print bytes_to_int(test)
