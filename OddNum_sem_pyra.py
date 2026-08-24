rows=int(input("Enter number "))
b=0
for i in range(0,rows):
    b=i*2+1
    for j in range(i+1):  # if i will be zero then 2nd for loop will not run
        print(b,end=" ")
    print()
