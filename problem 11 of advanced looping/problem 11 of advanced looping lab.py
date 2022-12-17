arr1 = []
arr2 = []
arr_cnt = []
cnt = 0
size1 = int(input("Enter the number of first array "))
for i in range(size1):
    arr1.insert(i, input())

size2 = int(input("Enter the number of second array "))
for i in range(size2):
    arr2.insert(i,input())

for i in range(size1):
    for j in range(size2):
        if arr1[i] == arr2[j]:
            cnt+=1
    arr_cnt.insert(i,cnt)
    cnt = 0

print("The repetition from first array to second array is: "+str(arr_cnt))