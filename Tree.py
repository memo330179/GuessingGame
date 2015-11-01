class TreeNode(object):
	def __init__(self, data = None, no = None, yes = None):
		"""Creates a tree with specified dataand reference to the left and right children"""
		self.item = data
		self.left = no
		self.right = yes

	def addLeft(self, data = None, no = None, yes = None):
		self.left = TreeNode(data, no, yes)

	def addRight(self, data = None, no = None, yes = None):
		self.right = TreeNode(data, no, yes)
	
	def getLeft(self):
		return self.left
	
	def getRight(self):
		return self.right
	
	def setValue(self, val):
		self.item = val

	def getValue(self):
		return self.item
	
