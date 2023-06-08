def generateDocument(characters, document):
    

    if document == "":
        return True
    temp = list(document.replace(" ",""))
    for i in characters:
        for j in list(temp):
            if i==" " or j==" ":
                pass
            elif i == j:
                temp.remove(j)


    if len(temp) == 0:
        return True
    else:
        return False
    

x = "Bste!hetsi ogEAxpelrt x "
y="AlgoExpert is the Best!"
print("Output is=",generateDocument(x,y))