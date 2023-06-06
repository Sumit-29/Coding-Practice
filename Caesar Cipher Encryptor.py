def caesarCipherEncryptor(string, key):
    # while key > 26:
    #     key = key -26

    # newString = ""
    # temp = ord(string[0])
    # length = len(string)
    # final = temp + length + key

    # for i in range(temp+key, final):
    #     if i > 122:
    #         newString += chr(i - 26)
    #     else:
    #         newString += chr(i)
    # return newString

    newLetters = ""
    newKey = key % 26
    for letter in string:
        newLetters += getNewLetter(letter, newKey)
    return newLetters

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    if newLetterCode <= 122:
        return chr(newLetterCode)
    else:
        return chr(96 + newLetterCode % 122)




x = "abc"
key = 52
print("Output is=",caesarCipherEncryptor(x,key))