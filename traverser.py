from a15 import guessingGame
from Tree import TreeNode
def main():
	player = guessingGame()
	
	player.readFile()
	play = "yes"
	while play == "yes":
		endR = player.present()
	
		if endR == 1:
			print "Yay!"
			play = raw_input("Would you like to play again?")
	if endR == 1:
		print"See you later!"
	elif endR == 0:
		player.addQuestion()
		player.writeFile()

main()
