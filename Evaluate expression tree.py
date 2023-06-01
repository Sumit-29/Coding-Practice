class tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



root = tree(-1)
root.left = tree(-2)
root.right = tree(-3)
root.left.left = tree(-4)
root.left.right = tree(2)
root.left.left.left = tree(2)
root.left.left.right = tree(3)
root.right.left = tree(8)
root.right.right = tree(3)



# Sample Output
#  6    -->   (((2 * 3) - 2) + (8 / 3))
def evaluateExpressionTree(root):
    # Write your code here.
    if root.value >=0:
        return root.value
    print("Root value:",root.value)
    leftValue = evaluateExpressionTree(root.left)
    rightValue = evaluateExpressionTree(root.right)
    
    print("Leftvalue = ",leftValue)
    print("RightValue = ",rightValue)
    print("\n")
    if root.value == -1:
        return leftValue + rightValue
    if root.value == -2:
        return leftValue - rightValue
    if root.value == -3:
        return int(leftValue / rightValue)
    
    return leftValue * rightValue
# print("Final Answer:")
print(evaluateExpressionTree(root))