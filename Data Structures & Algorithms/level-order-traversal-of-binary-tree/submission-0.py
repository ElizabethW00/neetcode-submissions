# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        out = []

        def addLevel(node, level):
            if not node:
                return
            if level == len(out):
                out.append([])
            out[level].append(node.val)
            addLevel(node.left, level + 1)
            addLevel(node.right, level + 1)
        
        addLevel(root, 0)
        return out