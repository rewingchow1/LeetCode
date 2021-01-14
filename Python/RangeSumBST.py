import null as null


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def rangeSumBST(root, L, R):


root = [10, 5, 15, 3, 7, null, 18]
L = 7
R = 15
out = rangeSumBST(root, L, R)
print(out)