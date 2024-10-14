class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: [TreeNode]):
    if root is None:
        return True
    return is_same(root.left,root.right)

def is_same(left_node,right_node):

    if left_node is None and right_node is None:
        return True
    if left_node is None or right_node is None:
        return False
    if left_node.val != right_node.val:
        return False
    return is_same(left_node.right,right_node.left) and is_same(left_node.left,right_node.right)
