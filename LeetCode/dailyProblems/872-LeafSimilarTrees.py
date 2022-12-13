# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # seq1
        nodes1 = []
        nodes1.append(root1)
        seq1 = []
        while (nodes1 != []):
            curr = nodes1.pop()
            if ( (curr.left==None) and (curr.right==None) ):
                # is leaf
                seq1.append(curr.val)
            if (curr.right != None):
                nodes1.append(curr.right)
            if (curr.left != None):
                nodes1.append(curr.left)
        # seq2
        nodes2 = []
        nodes2.append(root2)
        seq2 = []
        while (nodes2 != []):
            curr = nodes2.pop()
            if ( (curr.left==None) and (curr.right==None) ):
                # is leaf
                seq2.append(curr.val)
            if (curr.right != None):
                nodes2.append(curr.right)
            if (curr.left != None):
                nodes2.append(curr.left)
        # compare
        return seq1 == seq2