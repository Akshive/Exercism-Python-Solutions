def isTriangle(sides):
    sides.sort()
    if(sides[0] + sides[1] > sides[2]):
        return True
    return False

def equilateral(sides):
    if(isTriangle(sides) == True and sides[0] == sides[1] and sides[1] == sides[2]):
        return True
    return False


def isosceles(sides):
    if((isTriangle(sides) == True) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])):
        return True
    return False


def scalene(sides):
    if(isTriangle(sides) == False):
        return False
    if(isosceles(sides) == False):
        return True
    return False
