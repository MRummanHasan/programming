def binary_sort(sortedlist, n , x):
    start = 0
    end = n - 1

    while(start <= end):
        mid = int((start + end) / 2)
        if(x == (sortedlist[mid])):
            return mid
        elif(x < (sortedlist[mid])):
            end = mid - 1
        else:
            start = mid + 1
    return -1

n = input("Enter the size of list: ")
n = int(n)
sortedlist = []

for i in range(n):
    sortedlist.append(input("Enter %dth element: " %i))
x = input("Enter the number to search: ")
position = binary_sort(sortedlist, n, x)

if(position != -1):
    print("ENtered nmbr is present at position: " +str(position))
else:
    print("Entered nmbr is not present in the list")
