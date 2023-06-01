def getNthFib(n):
    # Write your code here.
    num1 = 0
    num2 = 1

    if n == 1 or n == 0:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,n):
            result = num1 + num2
            num1 = num2
            num2 = result
            
    return result

print("Nth Number is:",getNthFib(6))