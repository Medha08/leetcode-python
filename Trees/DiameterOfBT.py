class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.m = 0
        def findDiam(root):
            if(root == None):
                return 0
            if(root.left == None and root.right == None):
                return 1

            l = findDiam(root.left)
            r = findDiam(root.right)
            self.m = max(self.m,max(l+r,max(l,r)))

            return max(l,r)+1
        findDiam(root)
        return self.m