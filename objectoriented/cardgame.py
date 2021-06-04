import random
class Card:
  def __init__(self,suit,val):
   self.suit=suit
   self.value=val
  
  def show(self):
   print(str(self.value)+" of "+str(self.suit))

class Deck:
  def __init__(self):
   self.cards = []
   self.build()

  def build(self):
   for s in ["Spades","Clubs","Diamonds","Hearts"]:
     for v in range(1, 14):  
      self.cards.append(Card(s,v))
      #print(str(v)+" of "+str(s))	
  
  def show(self):
    for i in self.cards:
      i.show()

  def shuffle(self):
    for i in range(len(self.cards)-1, 0, -1):
      r = random.randint(0, i)
      self.cards[i] = self.cards[r]     
      self.cards[r] = self.cards[i]     
 
  def drawCard(self):
    return self.cards.pop()

class Player:
 def __init__(self, name):
   self.name = name
   self.hand = []
   
 def draw(self, deck):
   self.hand.append(deck.drawCard())
   return self

 def showHand(self):
   for j in self.hand:
     j.show()  



#card=Card("Clubs",4)
#card.show()

deck = Deck()
deck.shuffle()
#deck.show()


bib  = Player("Bibash")
bib.draw(deck).draw(deck).draw(deck)
bib.showHand()




