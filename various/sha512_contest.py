#!/usr/bin/env python2
# Attempt at a cryptographic hash function for the following contest:
# http://www.h11e.com/

import hashlib
from string import letters, digits
from random import randint, choice
from collections import Counter

chars = letters + digits
remembered_msgs = []

def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        return fn(*args, **kwargs)
    wrapper.called = 0
    wrapper.__name__ = fn.__name__
    return wrapper

@counted
def get_alt_msg():
    return get_alt_msg.called

def create_alt_hash():
    msg = str(get_alt_msg())
    msg_512 = hashlib.sha512(msg).hexdigest()
    if msg_512.startswith("00000"):
        print msg, ":::", msg_512

def get_msg():
    size = randint(4,16)
    return ''.join(choice(chars) for x in xrange(size))
    
def create_hash():
    msg = get_msg() + "d3M!"
    print msg
    if not msg in remembered_msgs:
        msg_512 = hashlib.sha512(msg).hexdigest()
        if msg_512.startswith("00"):
            print msg, ":::", msg_512
        remembered_msgs.append(msg)
        #~ count = Counter(msg_512)
        #~ if count["0"] > 20:
            #~ print msg, "\n", msg_512
        

#~ while 1:
create_hash()

#~ import hashlib
#~ import random
#~ import string
#~ 
#~ def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    #~ return ''.join(random.choice(chars) for x in range(size))
#~ 
#~ if __name__ == '__main__':
    #~ curID = id_generator()
    #~ curHash = hashlib.sha512(curID).hexdigest()
    #~ for i in range(1000000000):
        #~ newID = id_generator()
        #~ newHash = hashlib.sha512(newID).hexdigest()
        #~ if newHash < curHash:
            #~ curID = newID
            #~ curHash = newHash
            #~ if i > 100000:
                #~ with open(curID, 'w+') as fp:
                    #~ fp.write(curID + '\n' + curHash)
                #~ print curID
                #~ print curHash
#~ So I'd do something like:
#~ 
#~ def id_generator():
    #~ return random.randrange(10**25)
#~ if __name__ == '__main__':
    #~ for x in itertools.count(id_generator(), step=93):
        #~ hash = hashlib.sha512('%X' % x).hexdigest()
        #~ [...]
#~ 
#~ itertools.count will keep going forever, so you can just let it run until you win the contest.


#~ import hashlib
#~ import itertools
#~ def dicAttack():
#~ #wordlist = raw_input('\nenter path')
#~ wordlist = "C:/Users/LolReadingMyUser/Desktop/programming/Java Side Projects/Word lists/realhuman_phill (2).txt"
#~ try:
    #~ words = open(wordlist, "r")
#~ except(IOError):
    #~ print "Error in reading the word list. Please check your path and try again."
    #~ sys.exit(1)
#~ 
#~ words = words.readlines()
#~ print 'there are ' + str(len(words)) + ' words in your word list.\n'
#~ for word in words:
    #~ hash = hashlib.sha512()
    #~ hash.update(word);
#~ 
    #~ value = hash.hexdigest()
    #~ if value.startswith("0000000"):
        #~ print value
        #~ print word
#~ 
#~ 
#~ 
#~ def bruteforce(charset, maxlength):
     #~ return (''.join(candidate)
            #~ for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
            #~ for i in range(1, maxlength + 1)))
#~ 
#~ 
#~ if __name__ == '__main__':
    #~ for attempt in bruteforce("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&* ()_+", 5):
#~ 
    #~ hash = hashlib.sha512(attempt)
#~ 
    #~ value = hash.hexdigest()
    #~ if value.startswith("000000000"):
        #~ print value
        #~ print attempt

#~ import hashlib
#~ import random
#~ import string
#~ 
#~ def generate_challenger(size=29, chars=string.ascii_uppercase + string.digits):
    #~ return ''.join(random.choice(chars) for x in range(size))
#~ 
#~ if __name__ == '__main__':
    #~ champion = "unknown"
    #~ championHash = "0000000000647bbda32e45f07bcf18b6dfa2c8fbfd9f4f5257a591abc951a0c977fde6a43dd0f0423bd8cbb9b0110b3f0a7bf849458b8acb0b00de2347b20270"
    #~ while True:
        #~ challenger = generate_challenger()
        #~ challengerHash = hashlib.sha512(challenger.encode('utf-8')).hexdigest()
        #~ if challengerHash < championHash:
            #~ break
    #~ print(challenger)
    #~ print(challengerHash)

#~ import hashlib
#~ import random
#~ 
#~ winner="0000000000647...get from website";
#~ while 1:
    #~ rnd = '%030x' % random.randrange(16**30)
    #~ m = hashlib.sha512(rnd).hexdigest();
    #~ if m < winner:
        #~ print rnd
