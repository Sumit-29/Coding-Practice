def runLengthEncoding(string):
    count = 0
    temp =""
    result =""
    for i in string:
        
        if temp != i:
            # print("Printing i =",i)
            result += str(count)
            result += temp
            temp = i
            count = 1
        elif count == 9: 
            result += str(count)
            result += temp
            temp = i
            count = 1
        else:
            count += 1
    result += str(count)
    result += temp
    return result[1:]



x = "AAAAAAAAAAAAABBCCCCDD"
print("Output ==",runLengthEncoding(x))