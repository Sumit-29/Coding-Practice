def commonCharacters(strings):
    
    length = float('inf') 
    index = 0
    result = []
    
    for i in range(len(strings)):
        if length > len(strings[i]):
            length = len(strings[i])
            index = i
    
    for i in strings[index]:
        result.append(i)

    for i in strings:
        for char in list(result):

            if char not in i:
                result.remove(char)
            
            if len(result) == 0:
                break


    return set(result)

x = ["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]

# x =  ["*abcd", "def*", "********d*******"]
print("output is=",commonCharacters(x))