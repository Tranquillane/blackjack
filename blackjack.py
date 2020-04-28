import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card(object):
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def value(self):
		if self.rank in ['J', 'Q', 'K']:
			return 10
		elif self.rank == 'A':
			return 11
		else:
			return int(self.rank)

	def __str__(self):
		return self.rank + ' of ' + self.suit

class Deck:
	def __init__(self):
		self.cards = []
		for s in suits:
			for r in ranks:
				self.cards.append(Card(s, r))

	def shuffle(self):
		random.shuffle(self.cards)

	def show(self):
		for c in self.cards:
			print c
		print

	def draw(self, number_of_cards, hand):
		for i in range(number_of_cards):
			hand.append(self.cards.pop)
		#return self.cards.pop()

'''
	# probably don't use this
	def __str__(self):
		cards = []
		for c in self.cards:
			cards.append(str(c))
		return str(cards)
'''

class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def addCard(self, card):
		self.cards.append(card)
		self.value += card.value
		
		# ace score checker
		if card.rank == 'A':
			self.aces += 1
		while self.aces > 0:
			if self.value > 21:
				self.value -= 10
				self.aces -= 1


class Player(object):
	def __init__(self, money, bet):
		self.name = raw_input('What is your name?')
		self.hand = []
		self.money = money
		self.bet = bet
		self.isBust = False
		self.blackjack = False
		self.gameover = False

	def hit(self, deck):
		self.hand.append(Deck.draw())

	def showHand(self):
		for c in self.hand:
			print c
		print

	def discard(self):
		return self.hand.pop()

	def stand(self):
		return '%s score is %d' % [self.name, self.score]

	def bust(self):
		if self.value > 21:
			self.isBust = True
			print '%s gets bust!' % self.name
		else:
			self.stand()


class Dealer(Player):
	def __init__(self):
		self.name = raw_input('What is your name?')
		self.hand = []
		self.money = money

def game():
	deck = Deck()
	player = Player()
	dealer = Dealer()