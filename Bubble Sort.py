def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
        

                
list=[23,543,1,8,3]
print(bubble_sort(list))
                
            
            