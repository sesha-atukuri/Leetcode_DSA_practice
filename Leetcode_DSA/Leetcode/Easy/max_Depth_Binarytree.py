from poetry.console.commands import self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: [TreeNode]) -> int:
        return 0 if not root else 1 + max(maxDepth(root.left), maxDepth(root.right))

print(maxDepth([3,9,20,None,None,15,7]))