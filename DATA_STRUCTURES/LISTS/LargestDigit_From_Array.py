# Get the input from the user as a list map it to integer datatype
arr=list(map(int,input('Enter Array Elements : ').split()))
# create an empty list to store the reversed value 
arr1=[]

while arr:
    large=arr[0]
    for i in arr:
        if i>large:
            large=i
        else:
            continue
    arr1.append(large)
    arr.remove(large)
s="".join(str(x) for x in arr1)
print(s)
