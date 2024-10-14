def search_node_in_bst(root, value):

    # Write your code here.
    curr = root[0]
    while curr is not None:
        if  value == curr.key:
            return True
        elif value < curr.key:
            curr = curr.left
        else:
            curr = curr.right

    return False

print(search_node_in_bst([2,1,5],4))
