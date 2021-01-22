class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if(root == None or (not root.left and not root.right)):
            return root
        else:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
        return root
        