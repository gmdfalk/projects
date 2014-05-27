#! /usr/bin/env python2
#
# Help Nikola develop a password security check module for Sofia.
# The password will be considered strong enough if its length is greater than
# or equal to 10 symbols, it has at least one number, as well as containing one
# uppercase letter and one lowercase letter in it.

def checkio(data):
    
    if len(data) < 10 or not any(c.isdigit() for c in data):
        return False
    if not any(c.isupper() for c in data) or not any(c.islower() for c in data):
        return False
    return True

# Different solution
#checkio = lambda s: not(
        #len(s) < 10
        #or s.isdigit()
        #or s.isalpha()
        #or s.islower()
        #or s.isupper()
    #) 
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
