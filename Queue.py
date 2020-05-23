n = int(input('작업의 수 : '))
m = int(input('작업 번호 : '))
priority = list(map(int,input("우선순위를 입력하세요 : ").split()))
a = list(range(len(priority)))

time = 0

while True:
    if priority[0] == max(priority):
        time += 1
        if a[0] == m:
            print("소요 시간은 {0}분 입니다.".format(time))
            break
        else:
            priority.pop(0)
            a.pop(0)
    else:
        priority.append(priority.pop(0))
        a.append(a.pop(0))
        

