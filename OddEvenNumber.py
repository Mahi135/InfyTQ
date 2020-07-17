string=list(input("Enter the String: "))
even,odd,specialCharCount=[],[],0
for i in string:
    if i.isdigit():
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
    else:
        specialCharCount+=1
l=[]
if specialCharCount%2==0:
    for i in range(max(len(even),len(odd))-abs(len(even)-len(odd))):
        l.append(even.pop(0))
        l.append(odd.pop(0))
    if even!=[]:
        l.extend(even)
    if odd!=[]:
        l.extend(odd)
else:
    for i in range(max(len(even),len(odd))-abs(len(even)-len(odd))):
        l.append(odd.pop(0))
        l.append(even.pop(0))   
    if even!=[]:123@454578972@957486
        l.extend(even)
    if odd!=[]:
        l.extend(odd)
print(*l,end=" ")
