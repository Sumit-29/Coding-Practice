class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



root = BST(1)
root.left = BST(2)
root.right = BST(3)
root.left.left = BST(4)
root.left.right = BST(5)
root.left.left.left = BST(8)
root.left.left.right = BST(9)
root.left.right.left = BST(10)
root.right.left = BST(6)
root.right.right = BST(7)

def branchsum(root):
    # code here
    if root is None:
        return []
    visitedList = []
    result = []
    helper(root,visitedList,result)
    
    return result

def helper(root,vN,result):
    if root is None:
        return
    
    vN.append(root.value)
    if root.left is None and root.right is None:
      result.append(sum(list(vN)))
    helper(root.left,vN,result)
    helper(root.right,vN,result)
    vN.pop()

print("Sum of Branches is:",branchsum(root))