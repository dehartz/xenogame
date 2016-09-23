#Author: dehartz
#Program: xenomorph_invasion.py
#-----------------------------------------------------------------------------
from sys import exit

print "You are about to initialize into XENOMORPH INVASION."

name = raw_input("What is your name? \n > ")
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
                journey_1()
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
    morale = 0
    print """
    It worked! You hear the cries of pain and the gernade shrapnel rips through
    their chitinous exoskelton."""
    print "\nAlright Marines, we are LEAVING!"
    print """\n\nYou and your team head down the hallway.  \"Hey\" Sgt.Sansa said, jogging up next to you.
    \ndo you think we're gonna make it out of here?"
    1. Yes, don't worry.  I'll think of something.
    2. Honestly? Don't hold your breath, We'll be dead inside the hour.
    """
    answer = raw_input("> ")
    while True:
        if "1" in answer:
            morale += 1
            print "Sansa smiles at you, she looks reassured.\n"

            continue_game()
        elif "2" in answer:
            morale -= 1

            print "Sansa looks at you for a half second longer, then looks down at her"
            print "feet and walks ahead."
            continue_game()
        else:
            print "Answer the question, stupid."


def journey_2():
    morale_2 = 0
    text = "wigio"
    for i in range (0,25):
        print "\n"
    print """
    At the end of the hallway you come to a door.  On it is a jumble of 5 letters
    the text reads %s.  Above the text is an engraving of a muscular man with
    eyes like dark pools.  In his hand he has something round in shape, an apple?
    \"Looks like the door needs a password\" Pvt.Williams says in his nearly
    unintelligible southern accent.  \"Indeed, you driveling galooot.\" Xanarra
    fires back hotly.  She was clearly nearing her wits' end.  You turn and look at Xanarra.
    """ % text
    print "\n\t You don't appreciate Xanarra speaking so harshly to your crew..."
    print "But how do you want to handle this?\n"
    print """
    1.Rebuke Xanarra and remind her who is in charge.
    2.Try to calm everyone down, we need to be working as a team.
    """
    answer2 = raw_input("> ")
    while True:
        if "1" in answer2:
            morale_2 -= 1
            print """
            \"Xanarra! I don't give a damn who you are back at Federation One
            Out here you answer to me, and I don't EVER want to hear you talk
            to a member of my team like that again. Is that clear?\"

            Shanarra holds your gaze, her eyes hard as flint.  After a moment
            she looks away, saying nothing.
            """
            continue_game2()

        elif "2" in answer2:
            morale_2 += 1
            print """
            \"Guys, I know everyone is tired.  I am too.  Let's try and work
            together to get out of here.  We need to be working together as a team\"
            You see Xanarra relax slightly, some of the tension bleeding out of her.
            """
            continue_game2()

        else:
            print "Answer the question, stupid."


def continue_game():
    cont_inue = raw_input("Press enter to continue\n> ")
    if cont_inue == "":
        journey_2()
    else:
        print "Something went terribly wrong..."
        exit(0)

def continue_game2():
    cont_inue = raw_input("Press enter to continue\n> ")
    if cont_inue == "":
        door()
    else:
        print "Something went terribly wrong..."
        exit(0)

def door():
    print "This is where door will go"
    print "Change example"
    exit(0)



def dead(why):
    print why, "Oh well!"
    exit(0)

start()
