numA = float(input())
numB = float(input())
numC = float(input())

def Media(numA,numB,numC):
    if 0 > numA > 10 and 0 > numB > 10 and 0 > numC > 10 :
        return None 
    else:
        media = (numA * 2 + numB * 3 + numC * 5) / 10 
        return media
        
print("MEDIA = {:.1f}".format(Media(numA, numB, numC)))

