# CodeWars Title Case
def title_case(title, minor_words=""):
    # " ".join(minor_word[i] if word.lower() in minor_words.split().lower() for minor_word in minor_words else word for word in title.title().split())
    s = title.title()
    for word in s.lower().split()[1:]:  # ['clash','of','kings']
        for i, word in enumerate(minor_words.lower().split()):  #
            s = s.replace(word, minor_words.split().index(word))
    return s


"""
    for word in title.split()[1:]:
        if not minor_words:
            return title.title()
        else:
            for minor_word in minor_words.split():
                if word.lower() in minor_words.lower():
                    title = title.title().replace(
                        word, minor_word[minor_word.find(word)]
                    )
    # return title
    """


print(title_case(""), "")
print(title_case("a clash of KINGS", "a an the of"))  # "A Clash of Kings"
print(title_case("THE WIND IN THE WILLOWS", "The In"))  # "The Wind in the Willows"
print(title_case("the quick brown fox"))  # "The Quick Brown Fox"

# str.title()
# str.replace('DC', 'Marvel')
# [x for x in a if x in b]
