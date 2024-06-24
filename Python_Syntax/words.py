def print_upper_words(words):
    """Print out each word on a separate line, but in all uppercase

        For example:
        print_upper_words(["Learning", "Python"])
        LEARNING
        PYTHON
    """

    for word in words:
        print(word.upper())

print_upper_words(["Learning", "Python"])


def print_upper_words2(words):
    """Print words either in uppercase or lowercase that start with the letter ‘e’ on separate line

        For example:
        print_upper_words2(["Eritrea", "Mexico", "egg"])
        ERITREA
        EGG
    """

    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())

print_upper_words2(["Eritrea", "Mexico", "egg"])


def print_upper_words3(words, must_start_with):
    """Print words on a separate line that starts with the given letters.

        print_upper_words3(["hello", "hey", "goodbye", "wow", "yes"],
                   must_start_with={"h", "y"})
        HELLO
        HEY
        YES
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words3(["hello", "hey", "goodbye", "wow", "yes"], must_start_with={"h", "y"})