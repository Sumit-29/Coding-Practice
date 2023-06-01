def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    print("Red:",redShirtSpeeds)
    print("Blue:", blueShirtSpeeds)
    print(fastest)
    result = 0
    if fastest == "true":
        for i in range(len(redShirtSpeeds)):
            if redShirtSpeeds[i] > blueShirtSpeeds[len(redShirtSpeeds) - 1 -i]:
                result += redShirtSpeeds[i]
            else:
                result += blueShirtSpeeds[len(redShirtSpeeds) - 1 -i]
    else:
        for i in range(len(redShirtSpeeds)):
            if redShirtSpeeds[i] > blueShirtSpeeds[i]:
                result += redShirtSpeeds[i]
            else:
                result += blueShirtSpeeds[i]

    return result

x = [5,5,3,9,2]
y = [3,6,7,2,1]
fast = "false"
print(tandemBicycle(x,y,fast))
