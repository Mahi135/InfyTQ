n=int(input("Enter the matrix number(NxN)"))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n-1):
    for j in range(n-1):
        temp=[]
        temp.append(sum(list(map(int,list(str(arr[i][j]))))))
        temp.append(sum(list(map(int,list(str(arr[i][j+1]))))))
        temp.append(sum(list(map(int,list(str(arr[i+1][j]))))))
        temp.append(sum(list(map(int,list(str(arr[i+1][j+1]))))))
        if temp.count(temp[0])==len(temp):
            print()
            print(arr[i][j],arr[i][j+1])
            print(arr[i+1][j],arr[i+1][j+1])
            
