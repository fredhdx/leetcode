
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        res = []
        if not root:
            return res

        queue = [root]
        level = 0
        while queue:
            res.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return res

class Solution2:
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        
        level = [root]
        nextLevel = []

        while level:
            result.append([])
            for node in level:
                result[-1].append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level, nextLevel = nextLevel, []
        
        return result
