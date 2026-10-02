class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]
        mid = inorder.index(root_val)
        tree = TreeNode(root_val)
        tree.left = self.buildTree(preorder[1 : 1 + mid], inorder[0 : mid])
        tree.right = self.buildTree(preorder[1 + mid : ],inorder[mid + 1 : ])
        return tree