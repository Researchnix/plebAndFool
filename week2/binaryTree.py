# different kind of traversals
# level by level, breadth first
# depth first1: in order, left root right
# depth first2: pre order root left right
# depth first3: post order right left root

# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Fool:
    def diameterOfBinaryTree(self, root: TreeNode):
        if not root.left == None:
            a = self.diameterOfBinaryTree(root.left)
        if not root.left == None:
            b = self.diameterOfBinaryTree(root.right)
        return 0


exampleTree = TreeNode(1)
exampleTree.left = TreeNode(2)
exampleTree.right= TreeNode(3)
exampleTree.left.left = TreeNode(4)
exampleTree.left.right = TreeNode(5)


print("\n\n")
print(exampleTree.left.val)

f = Fool()
print(f.diameterOfBinaryTree(exampleTree))




