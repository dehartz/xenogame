#Author: dehartz
#Program: xenomorph_invasion.py
#-----------------------------------------------------------------------------
from sys import exit

print "You are about to initialize into XENOMORPH INVASION."

name = raw_input("What is your name? \n > ")
morale = 0
def start():
    print " You are Major %s" % name
    print """
    You and your team are trapped on BR55-B
    \nan uninhabited planet in the Soroan expanse
    \n\nYou are slowly coming to realize that the
    \nevents of the next few hours will mean the
    \ndifference between life and death.
    \n\n Your team consists of Sgt.Sansa, Pvt.Williams,
    \nand Fleet Admiral Xanarra.
    """
    thought_complete = False
    thought_meter = 0
    members = ["Pvt.Williams","Sgt.Sansa","Admiral Xanarra"]
    insults = ["Just shut up Private.","Sgt, please shut up.", "Admiral Please remain quiet."]
    k = 0
    j = k

    while True:

        k = (k+1) % len(members)
        prompt = "1.Get a move on.\n2.Tell %s to shut up.\n3.Keep Thinking of a plan\n> " % members[k]
        print "\"Well? Major %s? What should we do?\" %s asks in a whiny voice." % (name, members[k])
        decision = raw_input(prompt)

        if decision == "1":
            if thought_complete == False:
                print "\"Marines!\" you say.  \"We are LEAVING!\""
                dead("You and your team run headlong into a xenomorph ambush.")
            else:
                print """
                You decide to get ready and leave.  It occurs to you that the
                xenomorphs are probably preparing an ambush in the hallway
                leading out of the room you are in.  You decide to toss a gernade
                in there just in case.
                """
                journey()
        elif decision == "2":
            print insults[k]
        elif decision == "3":
            thought_meter +=1
            if thought_meter >= 3:
                print "I have thought enough."
                thought_complete = True
            else:
                print "You think intensely about a plan of escape."
        else:
            print "No comprendo homeslice."


def journey_1():
    prompt
    print """
    It worked! You hear the cries of pain and the gernade shrapnel rips through
    their chitinous exoskelton."""
    print "\nAlright Marines, we are LEAVING!"
    print """\n\nYou and your team head down the hallway.  \"Hey\" Sgt.Sansa said, jogging up next to me.
    \ndo you think we're gonna make it out of here?"
    1. Yes, don't worry.  I'll think of something.
    2. Honestly? Don't hold your breath, We'll be dead inside the hour.
    """
    answer = raw_input("> ")
    while True:
        if "1" in answer:
            morale += 1
            journey_2()
        elif "2" in answer:
            morale -= 1
            journey_2()
        else:
            print "Answer the question, stupid."

def journey_2()
            
    

def dead(why):
    print why, "Oh well!"
    exit(0)

start()
