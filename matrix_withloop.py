rows=int(input("enter the value of row:"))
colum=int(input("enter the value of colum:"))
matrix=[]
for o in range(rows):
    row=[]
    for i in range(colum):
        val=int(input(f"enter the value:{o}{i}:"))
        row.append(val)
    matrix.append(row)
for r in matrix:
    print(r)