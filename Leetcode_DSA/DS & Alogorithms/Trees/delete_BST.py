class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def deletebst(root, values_deleted):
    if root is None or len(values_deleted) == 0:
        return BinaryTreeNode(root)
    for value in values_deleted:
        root = delete_bst(root,value)

    return root

def delete_bst(root,key):
    if root is None:
        return root

    if key<root.value:
        root = delete_bst(root.left,key)
    elif key>root.value:
        root = delete_bst(root.right, key)
    else:
        #if root needs to be deleted
        if root.left is None and root.right is None:
            del root
            return None
        # node to be deleted has one child
        if root.right is None:
            temp = root.left
            return temp
        if root.left is None:
            temp = root.right
            return temp
        #node_to_be deleted has both child
        temp = root.right
        while temp.left is not None:
            temp = temp.left
        root.value = temp.value
        root.right = delete_bst(root.right,temp.value)
    return root

print(deletebst([4,2,6,1,3,5,7],[5,6]))


