###############################################################################################
#Name: Guessing Game
#
#Purpose: 
#To guess an animal you are thinking of and learn
#
#Attributions:
#This code uses a slightly modified version of the read recursion module provided by Dr. Nakazawa. The write recursion was also inspired by a talk in clas
# The tree was inspired by the book, but with some added functionality
###############################################################################################


from Tree import TreeNode
import read_recursion
import write_recursion

class guessingGame():
		"""This class runs the game from opening a file to writing back into it"""
	def __init__(self):
		"""Initialize the class with one empty node"""
		self.root = TreeNode()
		self.rootR = None # we use this for reference later

	def readFile(self):
		"""This functions reads the game.data file to get the knowledge so far"""
		fileN = open("game.data", "r")
		read_recursion.read_recursion(fileN, self.root)
		fileN.close()
	
	def present(self):
		"""Traverse through the tree going to a leaf"""
		self.rootR = self.root	#this is so that we dont lose the reference to the first node
		while self.rootR.left is not None and self.rootR.right is not None: #if this is not a guess then continue traversing
			usrinput = raw_input(self.rootR.getValue()) #ask a question
			if usrinput == "yes" and self.rootR.right is not None:				#go whichever way the user specifies
				self.rootR = self.rootR.right
			#	state = "y"
			elif  usrinput == "no" and self.rootR.left is not None:
				self.rootR = self.rootR.left
			#	state = "yes"
			else:
				break
		
		outp = self.rootR.getValue() #this is the leaf node being presenter
		state = raw_input(outp) #getting the user input

		if state == "yes": # we won
			print "I knew it"
			return 1

		elif state == "no": # we need to learn
			print "Aww"
			return 0
	def addQuestion(self):
		"""Adds question and two answers"""
		question = raw_input("What would you ask?")
		self.rootR.setValue(question)
		y=raw_input("What would the yes answer be? write in question form")
		n=raw_input("what would the no answer be? write in quation form")

		self.rootR.left = TreeNode(n)
		self.rootR.right = TreeNode(y)
	def writeFile(self):
		"""Write the end result to the file"""
		fileN = open ("game.data","w")
		write_recursion.write(fileN, self.root)
		fileN.close()
		# this doesn't work for some reason
		with open("game.data", "r+w") as f:
			for line in f:
				if line.strip():
					f.write(line)
