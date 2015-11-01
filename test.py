#######################################
#Name: Test.py
#purpose: This tests to make sure the tree and the write function are working
#Author: Guillermo
#
##########################################


from Tree import TreeNode
import write_recursion 
sampleTree = TreeNode()

sampleTree.setValue(7)



sampleTree.addLeft(6)
sampleTree.addRight(10)
y = sampleTree.getLeft()
x = sampleTree.getRight()
x.addLeft(9)
x.addRight(57)

y.addLeft(8)
y.addRight(47)


def print_tree(tree):
                if tree == None: 
                        return
                print tree.item
                print_tree(tree.left)
                print_tree(tree.right)

print_tree(sampleTree)

gameData = open("testData.txt", "w")

write_recursion.write(gameData, sampleTree)
