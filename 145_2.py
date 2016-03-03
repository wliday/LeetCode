class Solution(object):
    def postorderTraversal(self, root):
    	if not root: return []
    	stack = [root]
    	result = []
    	while stack:
    		node = stack.pop()
    		result.insert(0, node.val)
    		if node.left: 
    			stack.append(node.left)
    		if node.right:
    			stack.append(node.right)
    	return result
