#!/usr/bin/env python2

# Silly exercise to understand iterators with a very dirty approach to make sure
# we do research twice for every concept marking it as understood.

def does_understand(concept):
    if research.called in range(0,20,2):
        print "second cycle: '%s' \ndone" % concept
        print "-"*24
        understanding = True
        return understanding
    else:
        print "first cycle: %s" % concept
    
def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        return fn(*args, **kwargs)
    wrapper.called = 0
    wrapper.__name__ = fn.__name__
    return wrapper

@counted
def research(concept):
    "doing very import research"
    return concept

iteration_concepts = ["for","while","for in", "do while", "break", "continue"]
for concept in iteration_concepts:
    understanding = False
    while not understanding:
        knowledge = research(concept)
        understanding = does_understand(knowledge)
