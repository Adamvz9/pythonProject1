tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "TheEmperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "TheHermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19:"The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

fortune = {}

fortune["past"] = tarot.pop(13)

fortune["present"] = tarot.pop(22)

fortune["future"] = tarot.pop(10)

print(fortune)

for i, val in fortune.items():
    print ("Your", i, "is The", val, "Card")

import random

fortune = ('past', 'present','future')

for key in fortune.keys():
        remaining_cards = list(tarot.keys())
        choice = remaining_cards[random.randint(0, len(remaining_cards)-1)]
        fortune[key] = tarot.pop(choice)

for key, value in fortune.items():
        print("Your {} is the {} card" .format(key, value))


