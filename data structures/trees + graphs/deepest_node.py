# Given a binary tree, find the deep­est node in it.

class newNode:
    # constructor to create a new node
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    # maxLevel: keep track of max level seen so far
    # res : value of deepest node so far
    # level : level of root
    def find(root,level,maxLevel,res):

        if (root != None):
            level += 1
            find(root.left, level, maxLevel, res)

            #update level and valDeepest
            if (level > maxLevel[0]):

                res[0] = root.data
                maxLevel[0] = level
