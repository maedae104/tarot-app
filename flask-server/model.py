
def get_minor_arc(suit):

    minor_arcana = {}
    for i in range(1,15):
    
        if i == 1: 
            i = "Ace"
            minor_arcana[i] = suit
        
        elif i == 11: 
            i = "Page"
            minor_arcana[i] = suit

        elif i == 12: 
            i = "Knight"
            minor_arcana[i] = suit
        
        elif i == 13: 
            i = "Queen"
            minor_arcana[i] = suit
        
        elif i == 14: 
            i = "King"
            minor_arcana[i] = suit

        else:
            minor_arcana[i] = suit
        
        
    return minor_arcana

major_arcana = {
    0: "The Fool",
    1: "The Magician",
    2: "The High Pristess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Strength",
    10: "Wheel of Fortune",
    11: "Justice",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World"
}


def build_deck():
    deck = { "MajorArcana": major_arcana,
            "Swords" : get_minor_arc("Swords"),
            "Wands" : get_minor_arc("Wands"),
            "Pentacles" : get_minor_arc("Pentacles"),
            "Cups" : get_minor_arc("Cups")
            } 
    
    return deck


print(build_deck())