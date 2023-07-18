dict ={}
x = "asdkdadk"
for i in x:
    # print(i)
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
for i in dict:
    print(dict[i])