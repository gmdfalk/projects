#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

"""Postapocalyptic Zombiegame
    1. Implement Fight Concept
    2. Add Equipment (Armor, Weapons) + Health + Stamina
    3. Add GameState and get rid of globals
    4. First attempt at classes, don't judge ;)
    5. sketch of a fight system:
    http://inventwithpython.com/blog/2012/03/18/how-much-math-do-i-need-to-know
    -to-program-not-that-much-actually/
"""

from random import randint
from sys import exit

class Colors(object):

    HEADER = '\033[95m'
    PLAYER = '\033[94m'
    FRIEND = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

        
class Player(object):

    def __init__(self, name):
        self.name = name
        self.health = 100

# Something funky is going on with the scope so we define these globally until
# this whole mess gets rewritten
cend = Colors().END
cyou = Colors().PLAYER
cfriend = Colors().FRIEND
    
class Enemy(object):
    pass

     
class Zombie(Enemy):
    pass

    
class ZombieDog(Enemy):
    pass

    
class HoodedFigure(Enemy):
    pass
    

class Scene(object):

    def __init__(self):
        # Same as above, can't figure out the scope problem, so this is a dirty
        # workaround
        player2 = Player("")
        self.npc = player2.name

    
class Street(Scene):

    def enter(self):
        print "You feel uneasy."
        action = raw_input("> ")
        if any(x in action for x in ("look", "explore")):
            pass


class Hospital(Scene):
    """ find some equipment here, maybe a first encounter """
    def enter(self):
        if not self.npc:
            print cfriend + "\"Wake up, man! We have to get out of here!\""\
                + cend
            print "Someone is shaking you angrily."
            print cfriend + "\"Finally, man, get up, we have to leave RIGHT NOW!\""\
                + cend
            print "As you come to, you realize you are in a hospital room."
            print "Your friend is grabbing you. You try to shake him off,"
            print "but your head is spinning. You can't even remember his name."
            friends_name = raw_input("What was his name again? ")
            player2 = Player(friends_name)
            self.npc = player2.name
            print "Right,", self.npc + "..."
            print "You've been friends since preschool."
            print cyou + self.npc, ", what the hell is going on here?" + cend
            print cfriend + "\"Can you get up? We need to get down the corridor"
            print "unless you want to die here.\"" + cend
        
        action = raw_input("> ")
        if any(x in action for x in ("look", "explore")):
            print "Nothing here yet"
            return "death"
        elif "door" in action:
            return "chained_door"
        elif any(x in action for x in ("hallway", "corridor")):
            return "street"
        elif "help" in action:
            print "try the door"
            return "hospital"
        else:
            return "hospital"

    
class ChainedDoor(Scene):
    def enter(self):
        print "As you approach the chained door you hear growling. A foul"
        print "stench fills the air. Someone sprayed graffiti on the door:"
        print "DON'T DEAD. OPEN INSIDE.\n What the hell does that mean?"
        action = raw_input("> ")
        if any(x in action for x in ("run", "flee", "back")):
            print ""
            return "hospital"
        else:
            print "As you stand there, pondering this mystery, something grabs"
            print "you at your ankle. You feel a searing pain.\n"
            return "death"


class Death(Scene):
    quips = [
        "You died. Sorry 'bout that.",
        "You died. Why? I don't know.",
        "Daaamn, he bit your face off."
    ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

    
class Fight(Scene):
    """ init, fight, flee """
    pass
    

class Engine(object):
    """ Starts the game by calling the opening scene and every scene after that """
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        your_name = raw_input("What is your name? ")
        player1 = Player(your_name)
        print cyou + "Your current HP is: ", player1.health, cend

        current_scene = self.scene_map.opening_scene()

        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Map(object):
    """ Gets and sets the name of the scenes (mapping them) """
    scenes = {
        "hospital": Hospital(),
        "chained_door": ChainedDoor(),
        "street": Street(),
        "death": Death(),
        "fight": Fight()
    }

    # Initialize as start_scene
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # And determine its corresponding class, then return it again to the Engine
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    # The very first scene, used when first initializing or starting over
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

zombie = Engine(Map("hospital"))
zombie.play()

