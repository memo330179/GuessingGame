#################################################################
#Name: traverser.py
#
#purpose: This drives the a15 and adds replay functionality
#
#Author: Guillermo Ramos Macias
#
#
#################################################################
from a15 import guessingGame
from Tree import TreeNode
def main():
	"""Drives the guessing game"""
	player = guessingGame() #initializes the game
	
	player.readFile() #reads the file
	play = "yes" 
	while play == "yes":# adds replay functionality
		endR = player.present()
	
		if endR == 1:
			print "Yay!"
			play = raw_input("Would you like to play again?")
	if endR == 1: #ends game
		print"See you later!"
	elif endR == 0: #learn
		player.addQuestion()
		player.writeFile()

main()
