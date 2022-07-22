class Card:
    shapes = ["Spades", "Hearts", "Clubs", "Diamonds"]
  
    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
 
    cards_values = {"Ace": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}

    def __init__(self , shape , card , value):
        self.shape = shape
        self.card = card
        self.value = value
    
    def printCard(self):
        print("{} of {}".format(self.value , self.shape))
