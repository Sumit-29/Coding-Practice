def transposeMatrix(matrix):
    result = []
    height = len(matrix[0])
    for a in range(height):
        list_name = []
        result.append(list_name)

    print("Printing result:",result)
    for i in matrix:
        for j in range(height):
            result[j].append(i[j])
    return result

x = [
    [1,2],
    [3,4],
    [5,6]]
print("Transpose output is=",transposeMatrix(x))
