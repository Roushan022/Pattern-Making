row=int(input("Enter a number "))
b=0
for i in range(row,0,-1):
    b=i
    for j in range(i):
        print(b,end=" ")
    print()
