# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        soma = 0
        nodes = []
        
        if (root == None): return 0
        
        if ((root.val >= low) and (root.val <= high)): soma += root.val
        if ((root.val >= low) and (root.left != None)): nodes.append(root.left)
        if ((root.val <= high) and (root.right != None)): nodes.append(root.right)
        
        while (nodes != []):
            curr = nodes.pop()
            if ((curr.val >= low) and (curr.val <= high)): soma += curr.val
            if ((curr.val >= low) and (curr.left != None)): nodes.append(curr.left)
            if ((curr.val <= high) and (curr.right != None)): nodes.append(curr.right)
        
        return soma