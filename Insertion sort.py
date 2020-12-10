
arrayIn = [4, 1, 6, 9, 0, 2]

for i in range(1, len(arrayIn)):
    key = arrayIn[i]
    j = i-1
    while (j >= 0 and arrayIn[j] > key):
        arrayIn[j+1] = arrayIn[j]
        j = j-1
        arrayIn[j+1] = key
print(arrayIn)
