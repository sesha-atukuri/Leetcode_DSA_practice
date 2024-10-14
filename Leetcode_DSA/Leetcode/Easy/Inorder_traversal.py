from poetry.console.commands import self


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: [TreeNode]):
        result =[]
        def dfs(curr_node, result):
            if not curr_node:
                return
            if curr_node.left:
                dfs(curr_node.left,result)
            result.append(curr_node.val)
            if curr_node.right:
                dfs(curr_node.right,result)
        dfs(root,result)
        return result
        '''print(result)

        #root_node = TreeNode(root[0])
        #if root:
        if root.left:
            self.inorderTraversal(root.left)
        print(root.left.val)
        result.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return result

        #return result'''





print(Solution.inorderTraversal(self,TreeNode([1,None,2,3])))