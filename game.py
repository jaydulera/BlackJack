from deck import Deck
from player import Player

class Game:

    game = None

    def __init__(self , nameOne , nameTwo):
        self.playerOne = Player(nameOne)
        self.playerTwo = Player(nameTwo)
        self.deck = Deck()
        # self.turn = 0
    
    @staticmethod
    def createGame(nameOne , nameTwo):
        if Game.game != None:
            return Game.game
        else:
            Game.game = Game(nameOne , nameTwo)
            return Game.game

    
    def startGame(self):
        self.deck.getCards()
        self.begin()
    
    def begin(self ,  passCount = 0):

        while True:
            #Player One Turn
            action = input("\nEnter hit to draw one card and pass to skip\n")
            if action == 'hit':
                passCount = 0
                newCard = self.deck.draw()
                self.playerOne.hit(newCard)
                newCard.printCard()
                checkOne = self.playerOne.check()
                self.playerOne.getScore()
                if checkOne == "Win":
                    print("Congralutations, {} wins!" .format(self.playerOne.name))
                    break
                elif checkOne == "Over":
                    print("Congralutations, {} wins!".format(self.playerTwo.name))
            else:
                if passCount == 1:
                    if self.playerOne.score > self.playerTwo.score:
                        print("Congralutations, {} wins!" .format(self.playerOne.name))
                    else:
                        print("Congralutations, {} wins!".format(self.playerTwo.name))
                else:
                    passCount += 1
                    
            #Player 2's turn
            action = input("\nEnter hit to draw one card and pass to skip\n")
            if action == 'hit':
                newCard = self.deck.draw()
                self.playerTwo.hit(newCard)
                newCard.printCard()
                checkOne = self.playerTwo.check()
                self.playerTwo.getScore()
                if checkOne == "Win":
                    print("Congralutations, {} wins!".format(self.playerTwo.name))
                    break
                elif checkOne == "Over":
                    print("Congralutations, {} wins!" .format(self.playerOne.name))
            else:
                if passCount == 1:
                    if self.playerOne.score > self.playerTwo.score:
                        print("Congralutations, {} wins!" .format(self.playerOne.name))
                    else:
                        print("Congralutations, {} wins!".format(self.playerTwo.name))
                else:
                    passCount += 1

game = Game.createGame("Jay" , "Ajay")
game.startGame()




        