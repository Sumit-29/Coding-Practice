def classPhotos(redShirtHeights, blueShirtHeights):
    # Write
    redShirtHeights.sort()
    blueShirtHeights.sort()
    red = sum(redShirtHeights)
    print("Sum of red:", red)
    blue = sum(blueShirtHeights)
    print("Sum of blue:", blue)
    if red > blue:
        print("In red Looop")
        for i in range(len(redShirtHeights)):
            if blueShirtHeights[i] > redShirtHeights[i] or blueShirtHeights[i] == redShirtHeights[i]:
                print("False")
                # return False
    else:
        print("In blue Looop")
        for i in range(len(redShirtHeights)):
            print("Blue value:",blueShirtHeights[i])
            print("red value:",redShirtHeights[i])
            if (blueShirtHeights[i] < redShirtHeights[i]) or (blueShirtHeights[i] == redShirtHeights[i]):
                print("False")
                # return False
            
    # return True
    print("True")
    
x = [6, 9, 2, 4, 5, 1]
y = [5, 8, 1, 3, 4, 9]
classPhotos(x,y)