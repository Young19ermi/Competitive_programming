class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        def solve(node,index):
            if node:
                solve(node.left,index+1)
                solve(node.right,index+1)
                levels[index].append(node.val)
            res = 0
            for key,items in levels.items():
                res += len(items)
            return res
        return solve(root,0)

