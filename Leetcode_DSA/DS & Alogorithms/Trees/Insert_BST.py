class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def build_a_bst(values):
    """
Args:
values(list_int32)
Returns:
BinaryTreeNode_int32
"""
# Write your code here.
    root = None
    for value in values:
        root = insert_bst(root,value)


    return root

def insert_bst(root,value):
    if root is None:
        return BinaryTreeNode(value)
    parent_node = root
    current_node = root

    while current_node is not None:
        parent_node = current_node
        if current_node.value < value:
            current_node = current_node.right
        else:
            current_node = current_node.left

    if parent_node.value < value:
        parent_node.right = BinaryTreeNode(value)
    else:
        parent_node.left = BinaryTreeNode(value)

    return root

print(build_a_bst([7, 5, 9]))

