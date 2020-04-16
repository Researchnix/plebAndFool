class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Pleb:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def maxDepth(node) -> int:
            if not node:
                return 0

            return max(maxDepth(node.left), maxDepth(node.right)) + 1

        diameterThroughRoot = maxDepth(root.left) + maxDepth(root.right)
        return diameterThroughRoot
