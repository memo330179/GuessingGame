from Tree import TreeNode
import read_recursion
import write_recursion

class guessingGame():
	def __init__(self):
		self.root = TreeNode()
		self.rootR = None

	def readFile(self):
		fileN = open("game.data", "r")
		read_recursion.read_recursion(fileN, self.root)
		fileN.close()
		self.rootR = self.root
	def present(self):
		
		while self.rootR.left is not None and self.rootR.right is not None:
			usrinput = raw_input(self.rootR.getValue())
			if usrinput == "yes" and self.rootR.right is not None:
				self.rootR = self.rootR.right
			#	state = "y"
			elif  usrinput == "no" and self.rootR.left is not None:
				self.rootR = self.rootR.left
			#	state = "yes"
			else:
				break
		
		outp = self.rootR.getValue()
		state = raw_input(outp)

		if state == "yes":
			print "Hooray"
			return 1

		elif state == "no":
			print "Aww"
			return 0
	def addQuestion(self):
		question = raw_input("What would you ask?")
		self.rootR.setValue(question)
		y=raw_input("What would the yes answer be?")
		n=raw_input("what would the no answer be?")

		self.rootR.left = TreeNode(n)
		self.rootR.right = TreeNode(y)
	def writeFile(self):
		fileN = open ("game.data","w")
		write_recursion.write(fileN, self.root)
		fileN.close()
		with open("game.data", "r+w") as f:
			for line in f:
				if line.strip():
					f.write(line)
