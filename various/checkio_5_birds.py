#! /usr/bin/env python2

# When I start to feed my pigeon, a minute later two more fly by. And a minute
# later another 3. Then 4, and so on.
# One portion of food lasts a pigeon for a minute. In case there's not enough
# food for all the birds, the pigeons that came first, eat first.
# Pigeons are hungry animals and eat without stopping. If I have N portions
# of wheat, how many pigeons will be fed with at least one portion of wheat? 

def checkio(wheat):
    assert 0 < wheat < 100000
    if wheat <= 2:
        return 1
    new_birds = 0
    
    for i in range(1, wheat):
        old_birds = new_birds
        new_birds += i
        if wheat == 0:
            return old_birds
        elif wheat >= new_birds:
            wheat -= new_birds
        elif wheat >= old_birds:
            return wheat
        else:
            return old_birds
            
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"

