class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0], None, None)
        for i in range(1, len(tree_data)):
            self.add(tree_data[i])
    
    def add(self, val):
        node = self.root
        while(node != None):
            if(node.data < val):
                if(node.right == None):
                    node.right = TreeNode(val, None, None)
                    return
                else:
                    node = node.right
                
            else:
                if(node.left == None):
                    node.left = TreeNode(val, None, None)
                    return
                else:
                    node = node.left

    def data(self):
        return self.root

    def sorted_data(self):
        ans = []
        self.inorder_traversal(self.root, ans)
        return ans
        
    def inorder_traversal(self, node, ans):
        if(node == None):
            return
        self.inorder_traversal(node.left, ans)
        ans.append(node.data)
        self.inorder_traversal(node.right, ans)