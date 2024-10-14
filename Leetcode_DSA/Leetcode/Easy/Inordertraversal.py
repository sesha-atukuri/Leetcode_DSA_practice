class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class solution:
    def inorder_traversal(root:TreeNode):

        return solution.inorder_traversal(root.left) + [root.val] + solution.inorder_traversal(root.right) if root else []

print(solution.inorder_traversal([1,None,2,3]))