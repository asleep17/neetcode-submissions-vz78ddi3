# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            qlen=len(q)
            level=[]                      
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
"""
For tracing 
    3
   /  \
   9   20
       /  \
       15  7
q=[3]
qlen=5
level=[]
for i in range 5:
    node=9
    if 3:
        level=[3]
        q[9,20]
level=[3]
"""
        