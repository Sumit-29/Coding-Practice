# Input = [x, [y, [z]]]
# O/P = x + 2 * (y + 3z)

def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier


x = [5,2,[7,-1],3,[6,[-13,8],4]]
print("Entering the value:",productSum(x))
    