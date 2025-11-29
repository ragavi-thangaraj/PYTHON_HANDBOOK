#Using built in method 

# arr=[4,3,5,6,7,8]
# k=3
# arr.sort()
# print(arr)
# print(arr[k-1])


# Without using Built in methods
#Get input from the User
arr=list(map(int,input('Enter array elements : ').split()))
#Get k
k=int(input('Enter K : '))


count=0
while arr:
    small=arr[0]
    for i in arr:
        if i<small:
            small=i
        else:
            continue
    arr.remove(small)
    count+=1
    if count==k:
        break
    else:
        continue
print('The Kth Smallest Element',small)

# Sample input output
# Enter array elements : 7 9 6 4 2 3
# Enter K : 4
# 6