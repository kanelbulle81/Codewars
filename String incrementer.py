# CodeWars - String incrementer


def isOfLengthFour(i):
    return True if len(i) == 4 else False


def isnum(x):
    return x.isdigit()


print(str(filter(isnum, "Foobar9009")))

# List of string
listOfStr = ["hi", "this", "is", "a", "very", "simple", "string", "for", "us"]
filteredList = list(filter(isOfLengthFour, listOfStr))

print("Filtered List : ", filteredList)


def increment_string(strng):
    alpha = "".join(char for char in strng if not char.isdigit())
    num = "".join(char for char in strng if char.isdigit())
    if num:
        if len(str(int(num) + 1)) < len(num):
            zeros = ""
            for i in range(len(num) - len(str(int(num) + 1))):
                zeros += "0"
            num = zeros + str(int(num) + 1)
        else:
            num = str(int(num) + 1)
    else:
        num = "1"

    return alpha + num
    # "".join(char for char in strng if char.isdigit())


def increment_string2(strng):
    return (
        strng + "1"
        if not strng[-1].isdigit()
        else strng + "".join(char for char in strng if char.isdigit())
    )
    # s = 'foo1'
    # s.replace(s[3], '3') >>> 'foo3'
    # s.replace(s[2:], '9') >>> 'fo9'

    # return [char for char in reversed(strng) if char.isdigit()}
    # return strng.replace(strng[len(strng) - len()])


print(increment_string2("foo"))
print(increment_string2("foobar001"))
print(increment_string2("foobar1"))
print(increment_string2("foobar00"))
print(increment_string2("foobar99"))
print(increment_string2("foobar099"))
print(increment_string2(""))
