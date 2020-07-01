""" CodeWars - Rot13 """

from string import ascii_lowercase, ascii_uppercase

alpha = ascii_lowercase + ascii_uppercase


def rot13(message):
    return "".join(c for c in message.split())


print(rot13("test"), "grfg")
print(rot13("Test"), "Grfg")

