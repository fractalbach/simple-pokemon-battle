

import random
import math
import sys


POKEMON_NAMES = []
with open("pokemon_names.txt", "r") as file:
	POKEMON_NAMES = file.read().split("\n")


class Pokemon:
	def __init__(self, name, hp, atk, defense):
		self.name = name
		self.maxhp = hp
		self.hp = hp
		self.atk = atk
		self.defense = defense
	
	def attack(self, other):
		r1 = random.random()
		r2 = random.random()
		damage = r1 * self.atk - r2 * other.defense
		damage = math.floor(damage)
		if damage < 0:
			print(f"{self.name} misses!")
			return
		other.hp -= damage
		print(f"{self.name} attacks {other.name} for {damage} damage!")
		

	def __repr__(self):
		koed = ""
		if self.hp <= 0: koed = "(KO)"
		return f"""
Name:   {self.name}
HP/MAX: {self.hp} / {self.maxhp}  {koed}
ATK:    {self.atk}
DEF:    {self.defense}
"""


def NewRandomPokemon(name):
	r = random.randint(0, 10)
	hp = random.randint(20, 30)
	atk = r + 5
	defense = 10 - r
	return Pokemon(name, hp, atk, defense)


def header1(title):
	print("_"*70)
	print(title, "\n" + "="*70)


def header2(title):
	print("_"*70)
	print(title, "\n" + "-"*70)


def wait():
	x = input("...")
	if x == "q": sys.exit()
	print()
	

def displayWinner(winner, loser):
	print(f"{loser.name} is defeated!")
	header1("THE BATTLE IS OVER")
	#header2("The Losing Pokemon:")
	print(loser)
	#header2("The Winning Pokemon:")
	print(winner)
	header1(f"WINNER: {p1.name}")
	
		
def BATTLE(p1, p2):
	header1("BATTLE BEGINS!")
	input("Press enter to begin...\n")
	i = 0
	while True:
		i += 1
		header2(f"ROUND {i}")
		p1.attack(p2)
		if p2.hp <= 0:
			p2.hp = 0
			displayWinner(p1, p2)
			break
		p2.attack(p1)
		if p1.hp <= 0:
			p1.hp = 0
			displayWinner(p2, p1)
			break
		#header2(f"HEALTH:")
		print()
		print(f"{p1.name}: {p1.hp}")
		print(f"{p2.name}: {p2.hp}")	
		wait()



def pokemon_generation_menu(i):
	header1(f"POKEMON {i}")
	name = random.choice(POKEMON_NAMES)
	p = NewRandomPokemon(name)
	print(p)
	return p


winner = None
p1 = pokemon_generation_menu(1)
p2 = pokemon_generation_menu(2)
BATTLE(p1, p2)



