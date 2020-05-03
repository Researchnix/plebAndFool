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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        a = self.diameterOfBinaryTree(root.left)
        b = self.diameterOfBinaryTree(root.right)
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(a, b, l + r + 2)

    def maxDepth(self, node) -> int:
        if not node:
            return -1
        return max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1




exampleTree = TreeNode(1)
exampleTree.left = TreeNode(2)
exampleTree.right= TreeNode(3)
exampleTree.left.left = TreeNode(4)
exampleTree.left.right = TreeNode(5)



f = Fool()
print(f.diameterOfBinaryTree(exampleTree))

#  The max depth of a single leaf is zero.
#  print(f.maxDepth(TreeNode(3)))

#  the example tree given on leetcode has max depth equal to 3 as
#  expected
#  print(f.maxDepth(exampleTree))
