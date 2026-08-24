rows=int(input("Enter a number "))
b=0
for i in range(rows+1,0,-1):
    b+=1
    for j in range(1,i):
        print(b,end=" ")
    print()
