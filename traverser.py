from a15 import guessingGame
from Tree import TreeNode
def main():
	player = guessingGame()
	
	player.readFile()
	

	endR = player.present()
	
	if endR == 1:
		print "Yay!"
	elif endR == 0:
		player.addQuestion()
		player.writeFile()

main()
