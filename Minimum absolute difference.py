'''
class Node:
    def __init__(self, val=1):
        self.val = val
        self.left = None
        self.right = None
'''

def min_diff(root):
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []

    values = inorder(root)
    min_difference = float('inf')
    for i in range(1, len(values)):
        min_difference = min(min_difference, values[i] - values[i - 1])
    return min_difference
