#! /usr/bin/env python3
#
# Return the most common letter in a string. If multiple letters tie at the top
# spot, return the one that comes first in the alphabet.

def checkio(text):
    import string
    from collections import Counter
    text = Counter([c.lower() for c in text if c in string.ascii_letters])
    freq = text.most_common(1)[0][1]
    return min([c for c, f in text.most_common() if f == freq])

    # Better solution with str.count()
    #text = text.lower()
    #return max(string.ascii_lowercase, key=text.count)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"CCcbbb!!!!") == "b", "Only letters."

