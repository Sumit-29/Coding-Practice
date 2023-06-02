def findThreeLargestNumbers(array):
    n1,n2,n3 = float('-inf'),float('-inf'),float('-inf')
    for i in array:
        
        if n1 < i:
            # print("Printing n1:",i)
            n3 = n2
            n2 = n1
            n1 = i  
        elif n2 < i:
            # print("Printing n2:",i)
            n3 = n2
            n2 = i
        elif n3 < i:
            # print("Printing n3:",i)
            n3 =i
    return [n3,n2,n1]

x = [141,1,17,-7,-17,-27,18,541,8,7,7]

print("Numbers are:",findThreeLargestNumbers(x))

