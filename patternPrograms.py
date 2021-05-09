"""
row=5
while row>=1:
    col=1
    while col<=row:
        print(1,end='')
        col+=1
    print()
    row-=1
-----------------------
row=5
while row>=1:
    col=1
    while col<=row:
        print(col,end='')
        col+=1
    print()
    row-=1
---------------------------
row=5
while row>=1:
    col=1
    while col<=row:
        print(row,end='')
        col+=1
    print()
    row-=1
-----------------------------
row =5
while row>=1:
    col=1
    while col<=row:
        print(row+col,end='')
        col+=1
    print()
    row-=1
---------------------------
row=5
while row>=1:
    col=0
    while col<row:
        print(row+col,end=' ')
        col+=1
    print()
    row-=1
----------------------------
row=5
while row>=1:
    col=1
    while col<=row:
        print(row+col,end=' ')
        col+=1
    print()
    row-=1
---------------------------
row=5
while row>=1:
    col=5
    while col>=row:
        print(col,end=' ')
        col-=1
    print()
    row-=1
----------------------------
row=5
while row>=1:
    col=5
    while col>=row:
        print(row,end=' ')
        col-=1
    print()
    row-=1
------------------------------
row=1
k=1
while row<=5:
    col=0
    while col<row:
        print(k,end=' ')
        k+=1
        col+=1

    print()
    row+=1
------------------------------
row=5
while row>=1:
    col=1
    while col<=row:
        print(col,end=' ')
        col+=1
    print()
    row-=1
-----------------------------
row=5
while row>=1:
    col=1
    while col<=row:
        print('-',end=' ')
        col+=1
    print()
    row-=1
----------------------------
k=1
row=5
while row>=1:
    col=1
    while col<=row:
        print('-',end=' ')
        col+=1
    else:
        print(k)

    row-=1
    k+=1
--------------------------
row=5
while row>=1:
    col=5
    while col>=row:
        print(row,end=' ')
        col-=1
    print()
    row-=1
---------------------------
row=1
k=5
while row<=5:
    col=1
    while col<=row:
        print(k,end=' ')
        col+=1
    print()
    row+=1
    k-=1
---------------------------
row=5
while row>=1:
    col=1
    while col<=row:
        print('-',end=' ')
        col+=1

    col2=5

    while col2>=row:
        print(row,end=' ')
        col2-=1
    print()
    row-=1
-----------------------------
row=5
while row>=1:
    col=5
    print('- '*row,end=' ')
    while col>=row:
        print(row,end=' ')
        col-=1
    print()
    row-=1
---------------------------
row=5
while row>=1:
    col2=1
    while col2<=row:
        print(' ',end=' ')
        col2+=1
    col=5
    while col>=row:
        print(row,' ',end=' ')
        col-=1
    print()
    row-=1
-------------------------------------"""
row=5
while row>=1:
    col2=1
    while col2<=row:
        print(' ',end=' ')
        col2+=1
    col=5
    k=1
    while col>=row:
        print(k,' ',end=' ')
        col-=1
        k+=1
    print()
    row-=1