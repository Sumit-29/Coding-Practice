def isPalindrome(string):
    temp = ""
    for i in reversed(string):
        temp += i
    if temp == string:
        return True
    else:
        return False
    
x = "abcdcba"

print("Output is=",isPalindrome(x))
