def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j]<arr[j-1] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1
    return arr
    

list=[233,23,43,1,2]
print(insertion_sort(list))
