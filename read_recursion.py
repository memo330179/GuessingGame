from Tree import TreeNode

def read_recursion(inFile, currentNode):
    """First argument is the handle to the file being read, and
    the second is the current node.
    Pre: currentNode has been created already, and inFile refers to a
         valid file that has been opened for reading.
    Post: currentNode will either have no children if it is a guess
          or two children if it is a question. Either the guess or
          the question will be saved in its 'data' instance variable."""
    category = inFile.readline()
    
    # continue to read from the file, eating up white space. Note that
    # readline() includes the newline at the end of the line in the file.
    # hence the '\n' after each possible value for category.
    while category != "Guess:\n" and category != "Question:\n":
        category = inFile.readline()

    data = inFile.readline()
    currentNode.setValue( data )
    
    # check for base case. If we are not at a question, we are at the
    # guesses in the leaves.
    if category != "Question:\n":
        return
    
    # we know now that this is an internal node. Read the order of the
    # directions. These two instructions are only necessary for files that
    # follow the format in the assignment text. If you assume a specific
    # ordering of the data, all these checks are not necessary.
    firstChild = inFile.readline()
    while firstChild != "no\n":
	firstChild = inFile.readline()
    #firstChild = inFile.readline()
    secondChild = inFile.readline()
    
    # first create the necessary child and then pass it to the recursion
    if firstChild == "no\n":
        currentNode.left = TreeNode()
        read_recursion( inFile, currentNode.left )
    else:
        currentNode.right = TreeNode()
        read_recursion( inFile, currentNode.right )

    # go the other route next
    if secondChild == "no\n":
        currentNode.left = TreeNode()
        read_recursion( inFile, currentNode.left )
    else:
        currentNode.right = TreeNode()
        read_recursion( inFile, currentNode.right )

