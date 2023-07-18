def generateDocument(characters, document):
    

    if document == "":
        return True
    # document = document.replace(" ","")
    # characters = characters.replace(" ","")
    tempdoc = {}
    tempchar = {}
    for i in document:
        if i not in tempdoc:
            tempdoc[i] = 1
        else:
            tempdoc[i] += 1
    # print(tempdoc)
    for i in characters:
        if i not in tempchar:
            tempchar[i] = 1
        else:
            tempchar[i] += 1
    # print(tempchar)
    for i in tempdoc:
        if i in tempchar:
            if tempdoc[i] <= tempchar[i]:
                pass
            else:
                return False
        else:
            return False
    return True


x = "helloworldO"
y="hello wOrld"
print("Output is=",generateDocument(x,y))   

