def linear_search(arr,x):
    for i in range(0,len(arr)):
        if arr[i]==x:
            return i
    return -1

list=[54,24,63,"a"]
print(linear_search(list,5))
