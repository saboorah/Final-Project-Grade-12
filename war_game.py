import random
import pygame
from pygameRogers import Game
from pygameRogers import Room
from pygameRogers import GameObject
from pygameRogers import TextRectangle
from pygameRogers import Alarm

#Craete a new game-------------------------------------------------------------
g = Game(900,500) 

#Color
BLUE = (0,143,213) 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
PASTEL_GREEN = (210,249,237)
DARK_GREEN = (14,99,73)

#Create Resources--------------------------------------------------------------
gameFont1 = g.makeFont("Arial",22)
gameBackground = g.makeBackground(BLUE)

diamondPics = []
for i in range (2,15):
    diamondPics.append(g.makeSpriteImage("Cards\DIAMONDS" + str(i) + ".jpg"))
    
heartPics = []
for i in range (2,15):
    heartPics.append(g.makeSpriteImage("Cards\HEARTS" + str(i) + ".jpg"))
    
spadePics = []
for i in range (2,15):
    spadePics.append(g.makeSpriteImage("Cards\SPADES" + str(i) + ".jpg"))
    
clubPics = []
for i in range (2,15):
    clubPics.append(g.makeSpriteImage("Cards\CLUBS" + str(i) + ".jpg"))
    
topCard = g.makeSpriteImage("Cards\TOP.jpg")

warCards = g.makeSpriteImage("Cards\TOP3.jpg")
#Create Room-------------------------------------------------------------------
r1  = Room("War",gameBackground)
g.addRoom(r1)

r2 = Room("War 2",gameBackground)
g.addRoom(r2)

#Classes for Game objects------------------------------------------------------
class Card (GameObject):
    def __init__(self, picture, value, suit):
        GameObject.__init__(self,picture)
        
        #Attributes
        self.value = value # 2-14
        self.suit = suit # H, D, C, S
        
    def update(self):
        self.checkMousePressedOnMe(event)
        
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP and not p1Card.war and len(p1Card.played) > 0 and len(p1_Deck.player_deck) > 0 and len(p2_Deck.player_deck) > 0: 
            
         
            lastCard = len(p1Card.played) - 1 
            card_p1_played = p1Card.played[lastCard]
            card_p2_played = p2Card.played[lastCard]
            
            
            if card_p1_played.value > card_p2_played.value:
                
                p1_war.war_count = 0
                
                if len(p1_war.card_list) > 0:
                        
                    p1_war.put_in_discard(p1_discard)
                    p2_war.put_in_discard(p1_discard)
                    
                    print("p1 ",p1_war)
                    print("p2 ",p2_war)
                
                p1Card.discardCard(card_p1_played)
                p2Card.discardCard(card_p2_played)
                
                p1_discard.addCard(card_p1_played)
                p1_discard.addCard(card_p2_played)
                
                
                
                print("Player 1 ",p1_discard)
                
            elif card_p1_played.value < card_p2_played.value:
                
                p1_war.war_count = 0
                
                if len(p2_war.card_list) > 0:
                      
                    p1_war.put_in_discard(p2_discard)
                    p2_war.put_in_discard(p2_discard)
                    
                    print("p1 ",p1_war)
                    print("p2 ",p2_war)
                
                
                p1Card.discardCard(card_p1_played)
                p2Card.discardCard(card_p2_played)
                
                p2_discard.addCard(card_p1_played)
                p2_discard.addCard(card_p2_played)
                
                
                
                print("Player 2 ",p2_discard)
                
            else:
                
                p1Card.war = True
                
                r1.addObject(p1_war)
                r1.addObject(p2_war)
                        
                
                p1_war.get_3_cards(p1_Deck)
                p2_war.get_3_cards(p2_Deck)
                
                p1_war.card_list.append(card_p1_played)
                p2_war.card_list.append(card_p2_played)
                
                print("p1: ",p1_war)
                print("p2: ",p2_war)
                
             #   print(p1_Deck)
              #  print(p2_Deck)
         #       print("Player 1 ",p1_discard)
         #       print("Player 2 ",p2_discard)
            
            self.mouseHasPressedOnMe = False
            
        
    def __str__(self):
        return str(self.value) + self.suit

class CardDeck(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        
        self.deck = []
        self.p1_deck = []
        self.p2_deck = []
        
        for i in range (0, len(diamondPics)):
            c = Card(diamondPics[i], (i+2), "D")
            self.deck.append(c)
            
        for i in range (0, len(heartPics)):
            c = Card(heartPics[i], (i+2), "H")
            self.deck.append(c)
            
        for i in range (0, len(clubPics)):
            c = Card(clubPics[i], (i+2), "C")
            self.deck.append(c)
            
        for i in range (0, len(spadePics)):
            c = Card(spadePics[i], (i+2), "S")
            self.deck.append(c)

        random.shuffle(self.deck)   
        
        #distribute the cards amoung the 2 players
        for i in range (0,len(self.deck)//2):
            self.p1_deck.append(self.deck[i])
            
        for i in range (len(self.deck)//2,len(self.deck)):
            self.p2_deck.append(self.deck[i])
        
        
        
    def __str__(self):
        s = ""
        
        for card in self.p1_deck:
            s += str(card) + " "
        s = "Deck1:\n" + s + "\n"
        
    
        s2 = ""
        
        for card in self.p2_deck:
            s2 += str(card) + " "
        s2 = "Deck2:\n" + s2 + "\n"
        
        return s + "\t\t\t\t" + s2
    
class PlayerDeck(GameObject):
    
    def __init__(self, picture, xPos, yPos, player_deck):
        GameObject.__init__(self,picture)
        
        self.rect.x = xPos
        self.rect.y = yPos
        
        self.player_deck = player_deck
   
        
        
    def __str__(self):
        s = ""
        
        for card in self.player_deck:
            s += str(card) + " "
        s = "Deck:\n" + s + "\n"
        return s
    
    def update(self):
        self.checkMousePressedOnMe(event)
        
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP  and len(p1_Deck.player_deck) > 0 and len(p2_Deck.player_deck) > 0 and (len(p1Card.played) == 0 or p1Card.war):   
                        
            card = p1_Deck.get_top_card()
            card2 = p2_Deck.get_top_card()
            
            if p1Card.war:
                
                x = 383 + ((p1_war.war_count - 1)*15)
           
                p2Card.war = True
                
                p1Card.flipCardOver(card,x)
                
                
                p2Card.flipCardOver(card2,x) 
                
                
                p1Card.war = False
                p2Card.war = False
            
            else:
                p1Card.flipCardOver(card)
                p2Card.flipCardOver(card2)    
              
                
                
            
            
     
         #   print(p1_Deck)
          #  print(p2_Deck)
            print(p1Card)
            print(p2Card)
            

          
            self.mouseHasPressedOnMe = False
      
    
    def get_top_card(self):
        
        if len(self.player_deck) > 0:
            c = self.player_deck[0]
            del self.player_deck[0]
            
            if len(self.player_deck) == 0:
                self.kill()
                
                
                restock = AddToDeckButton("Return Cards", 450, 200, gameFont1, DARK_GREEN, 200, 40, WHITE)
               
                r1.addObject(restock)
                    
        return c
    
    def addCard(self,card):
        self.player_deck.append(card)
        
     
    

class FlipedCard(GameObject):
    
    def __init__(self,xPos,yPos):
        GameObject.__init__(self)
        
        self.xPos = xPos
        self.yPos = yPos
        self.played = []
        
        self.war = False
        
        
    def flipCardOver(self,card,newX = None):
        
        
        if self.war:
            card.rect.x = newX 
        else:
            card.rect.x = self.xPos
        
        self.played.append(card)        
        
        card.rect.y = self.yPos
        
        r1.addObject(card)
            
            
        
    def discardCard(self, card):
        
        for c in self.played:
            c.kill()
    
        self.played.clear()

    def __str__(self):
         s = " cards flipped: "
         
         if len(self.played) > 0:
             for i in range (0,len(self.played)):
                 s += str(self.played[i]) + " "
             
         return s       
        
class Discardpile(GameObject):
    def __init__(self,xPos,yPos):
        GameObject.__init__(self)
        
        self.playedCards = []
        
        self.rect.x = xPos
        self.rect.y = yPos
        
    def addCard(self,card):
        self.playedCards.append(card)
        
        self.image = card.image
        
 ###################################################   
    def removeCards(self,playerDeck):
        for card in self.playedCards:
            playerDeck.addCard(card)
            
        random.shuffle(playerDeck.player_deck)
        
        self.playedCards.clear()
        self.image = pygame.Surface((0,0))
        self.kill()
 ######################################################       
    def __str__(self):
        s = ""
        if len(self.playedCards) > 0:
            for card in self.playedCards:
                s += str(card) + " "
        s = "discarded: " + s
        return s


class AddToDeckButton(TextRectangle):
    
    def __init__(self, text, xPos, yPos, font, textColor, buttonWitdth, buttonHeight, buttonColor):
    
        TextRectangle.__init__(self, text, xPos, yPos, font, textColor, buttonWitdth, buttonHeight, buttonColor)


    def update(self):
        
        self.checkMousePressedOnMe(event)
        
        if self.mouseHasPressedOnMe and event.type == pygame.MOUSEBUTTONUP:
            
            if len(p1_Deck.player_deck) == 0 and len(p1_discard.playedCards) == 0: 
                
                winner_label = TextRectangle("Game Over, Player 2 Won",500,210,gameFont1,PASTEL_GREEN)
                r2.addObject(winner_label)
                
                g.nextRoom()
                
                
                
            if len(p2_Deck.player_deck) == 0 and len(p2_discard.playedCards) == 0: 
                
                winner_label = TextRectangle("Game Over, Player 1 Won",500,210,gameFont1,PASTEL_GREEN)
                r2.addObject(winner_label)
                
                g.nextRoom()
            
            if len(p1_Deck.player_deck) == 0 and len(p1_discard.playedCards) != 0:
               p1_discard.removeCards(p1_Deck)
               r1.addObject(p1_Deck)
               r1.addObject(p1_discard)
               print("New P1 ",p1_Deck)
               
            if len(p2_Deck.player_deck) == 0 and len(p2_discard.playedCards) != 0: 
               p2_discard.removeCards(p2_Deck)
               r1.addObject(p2_Deck)
               r1.addObject(p2_discard)
               print("New P2",p2_Deck)
               
            self.kill()
            
class WarPile(GameObject):
    def __init__(self,picture,xPos,yPos):
        GameObject.__init__(self)
        
        self.war_count = 0
        
        self.rect.x = xPos
        self.rect.y = yPos
        self.picture = picture
        
        self.card_list = []
        
        self.timer = Alarm()
        
    def get_3_cards(self,playerDeck):
        
        if len(playerDeck.player_deck) > 4:
            
            self.image = self.picture
            
            for i in range (0,3):
                c = playerDeck.get_top_card()
                self.card_list.append(c)
                            
                
                
            self.war_count += 1
            
                       
        else:
            if p1_Deck == playerDeck:
                winner = "Player 2"
                loser = "Player 1"
                
            if p2_Deck == playerDeck:
                winner = "Player 1"
                loser = "Player 2"
                
            winner_label = TextRectangle(loser+" did not have enough cards for war, "+winner+" won",200,210,gameFont1,PASTEL_GREEN)
            r2.addObject(winner_label)
            self.timer.setAlarm(3000)
        
    def put_in_discard(self,p_discard):
        for i in range (0,len(self.card_list)):
            p_discard.addCard(self.card_list[i])
            
            
            self.card_list[i].kill()
            
            
        self.card_list.clear()
        self.kill()
    
    def update(self):
        if self.timer.finished():
            g.nextRoom()
            
    def __str__(self):
        s = ""
        
        for card in self.card_list:
            s += str(card) + " "
            
        s = "war pile: " + s
        return s
#Initialize Objects and add them to the room-----------------------------------

play_card_label = TextRectangle("Click either deck to flip cards",15,15,gameFont1,PASTEL_GREEN)
discard_card_label = TextRectangle("Click cards to collect",145,210,gameFont1,PASTEL_GREEN)


r1.addObject(play_card_label)
r1.addObject(discard_card_label)

d = CardDeck()
r1.addObject(d)

p1_Deck = PlayerDeck(topCard, 70, 50, d.p1_deck)
p2_Deck = PlayerDeck(topCard, 70, 350, d.p2_deck)

r1.addObject(p1_Deck)
r1.addObject(p2_Deck)

p1Card = FlipedCard(185,50)
p2Card = FlipedCard(185,350)

r1.addObject(p1Card)
r1.addObject(p2Card)

p1_discard = Discardpile(780,50) #when screen 900 pix, x = 730
p2_discard = Discardpile(780,350)

r1.addObject(p2_discard)
r1.addObject(p1_discard)

p1_war = WarPile(warCards, 265, 50)
p2_war = WarPile(warCards, 265,350)

r1.addObject(p1_war)
r1.addObject(p2_war)


#Start Game--------------------------------------------------------------------
g.start()


#Game Loop
while g.running:
    
    #Limit the game excecution framerate
    dt = g.clock.tick(60)
    
    #Check for events 
    for event in pygame.event.get():
        
        #Quit if user click [x]
        if event.type == pygame.QUIT:
            g.stop()
            
    #Update the gamestate of all objects
    g.currentRoom().updateObjects()
    
    #Render the background to the window surface
    g.currentRoom().renderBackground(g)
    
    #Render the object images to the background
    g.currentRoom().renderObjects(g)
    
    #Draw everything on the screen
    pygame.display.flip()
    
pygame.quit()