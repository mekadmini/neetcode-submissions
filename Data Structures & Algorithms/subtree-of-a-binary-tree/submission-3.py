# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serializeTree(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if node is None:
                result.append("#")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sr = "".join(self.serializeTree(subRoot))
        print(sr)
        r = "".join(self.serializeTree(root))
        print(r)
        return sr in r
        

        