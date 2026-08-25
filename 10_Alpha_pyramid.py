val=65
rows=int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(chr(val),end=" ")
        val+=1
    print()
    
