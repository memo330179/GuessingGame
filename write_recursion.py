def write(inFile, currentNode):
	if currentNode.right is not None and currentNode.left is not None:
		inFile.write("Question:\n")
	else:
		inFile.write("Guess:\n")
	inFile.write(str(currentNode.getValue())+"\n")

	if currentNode.right is None and currentNode.left is None:
		return
	inFile.write("no\n")
	inFile.write("yes\n")
	write(inFile, currentNode.left)

	write(inFile, currentNode.right)
