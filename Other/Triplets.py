# Program Name: Triplets
# Date: 3/03/2022
# Programmer: Leo
# Description: To make a randomized 3 line poem using python lists and the random function

import random

# our lists of words
noun = ["actor", "gold", "grass", "parrot", "afternoon", "pencil", "hair", "pillow", "army", "honey", "balloon", "horse", "queen", "quill", "house", "rain", "beach", "ice", "bed", "boy", "river", "branch", "island", "rocket", "room", "brother", "jelly", "rose", "candle", "car", "juice", "school", "scooter", "king", "shampoo", "shoe", "kite", "soccer", "church", "knife", "spoon", "lamp", "stone", "ghost"]
pastVerb = ["arose", "awoke", "bore", "beat", "became", "began", "bent", "bound", "bled", "broke", "brought", "built", "caught", "chose", "clung", "cut", "crept", "crept", "drew", "drank", "ate", "fell", "fought", "found", "flew", "forgot", "forgave", "gave", "went", "grew", "hung", "heard", "hid", "kept", "led", "lied", "lost", "made", "met", "paid", "rose", "ran", "sawed", "saw", "sent", "showed", "slid", "spoke", "swept", "swam", "swung", "tore", "threw", "wept", "won", "wrote"]
presentVerb = ["arise", "awake", "bear", "beat", "become", "begin", "bend", "bet", "bite", "bleed", "break", "broadcast", "build", "burn", "can", "choose", "cling", "come", "creep", "dig", "dive", "draw", "dream", "drink", "feed", "fall", "eat", "feed", "fight", "find", "fly", "foresee", "forgive", "freeze", "get", "give", "grow", "have", "hide", "hit", "keep", "know", "lean", "learn", "let", "lie", "mow", "pay", "put", "quit", "read", "ring", "saw", "run", "see", "sell", "shake", "shoot", "sleep", "smell", "split", "swing", "tear", "wake", "weep", "write"]
rhymingList = [["cat", "hat", "bat"], ["owl", "towel", "trowel"], ["rock", "chalk", "hawk"], ["boat", "coat", "stoat"], ["lake", "rake", "flake"], ["dump", "bump", "lump"], ["hole", "mole", "troll"], ["pot", "knot", "cot"], ["cook", "book", "hook"], ["seed", "creed", "weed"], ["map", "sap", "lap"], ["whip", "rip", "lip"], ["bird", "herd", "curd"], ["hill", "will", "bill"], ["hide", "tide", "guide"], ["cow", "plow", "bow"]]
# noun[x] rhymes with rhymingNoun[x]

# the layout of the poem
'''
The <noun> <past verb> to the <rhyming noun>
So it could <present verb> the <rhyming noun>
But it was a <rhyming noun>
'''

# pop a random word out of each list and save it into a variable
nounUsed = noun.pop(random.randrange(0, len(noun)-1))
pastVerbUsed = pastVerb.pop(random.randrange(0, len(pastVerb)-1))
presentVerbUsed = presentVerb.pop(random.randrange(0, len(presentVerb)-1))

# pop a random LIST out of our list of lists and save it to a new a variable
rhymingNoun = rhymingList.pop(random.randrange(0, len(rhymingList)-1))

# shuffle the list for randomness
random.shuffle(rhymingNoun)

# print our poem with the new variables filling the blanks
print("The", nounUsed, pastVerbUsed, "to the", rhymingNoun[0])
print("So it could", presentVerbUsed, "the", rhymingNoun[1])
print("But it was a", rhymingNoun[2])
