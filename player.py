from unicodedata import name


class Player:
    def __init__(self , name):
        self.name = name
        self.cardsList = []
        self.score = 0
    
    def hit(self , card):
        if card.value == 11:
            if self.score <= 10:
                self.cardsList.append(card)
                self.score += card.value
            else:
                self.cardsList.append(card)
                self.score += 1
        else:
            self.cardsList.append(card)
            self.score += card.value
    
    def check(self):
        if self.score < 21:
            return 'Under'
        elif self.score == 21:
            return "Win"
        else:
            return "Over"
    def getScore(self):
        print("Your current score is {}".format(self.score))
    
