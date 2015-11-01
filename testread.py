from Tree import TreeNode
import read_recursion
gameTree = TreeNode()
fileN = open("testData.txt", "r")
read_recursion.read_recursion(fileN, gameTree)

def print_tree(tree):
	if tree == None:
		return
	print tree.item
	print_tree(tree.left)
	print_tree(tree.right)

print_tree(gameTree)
