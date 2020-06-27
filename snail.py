def snail(c, cnt, x, y):     
    if x>0 and y>0:                  
        for i in range(c, c+y):
            cnt += 1
            b[c][i] = cnt
        for i in range(c+1, c+x):
            cnt += 1
            b[i][c+y-1] = cnt
        for i in range(c+y-2,c-1,-1):
            cnt += 1
            b[c+x-1][i] = cnt
        for i in range(c+x-2,c,-1):
            cnt += 1
            b[i][c] = cnt

        c = c + 1
        x = x - 2
        y = y - 2
        cnt == cnt

    else:
        return 
        
    snail(c, cnt, x, y)

a = int(input("숫자를 넣으시오 : "))
b = [[0]*a for i in range(a)]
c = 0
cnt = 0
x = a
y = a
snail(c, cnt, x, y)
for i in range(0,a):
    for j in range(0,a):
        print(b[i][j],end=',')
    print()