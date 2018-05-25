def LinearSearch(list, value):
    position = 0
    found = False
    for v in list:
        if(v==value):
            found = True
            return found
    return False;

def BinarySearch(list, value):
    found = False
    first = 0
    last = len(list)
    while not found and first <= last:
        midpoint = int((first + last)/2)
        if(list[midpoint] == value):
            found = True
        else:
            if first >= last:
                found = False
            else:
                if list[midpoint] > value:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
    return found

a = [3,5,6,8,2,10]

print(a[:2])
print(a[2:])
print(a)
print(list(a).sort())
test = BinarySearch(a, 5)
if test == True:
    print('Found')
else:
    print('Not found')
