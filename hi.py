print('========== 메뉴 ==========')
print('PUSH : 1')
print('POP : 2')
print('SHOW : 3')
print('(종료하려면 1,2,3 이외의 수 입력)')

stack_list = []
while True:
    menu = int(input('메뉴를 선택하세요 : '))

    if menu == 1:
        push = int(input('수 입력 : '))
        stack_list.append(push)
    elif menu == 2:
        if not stack_list:
            print('입력된 데이터가 없습니다.')
        else :
            stack_list.pop()
    elif menu == 3:
        print(stack_list)
    else:
        print('==========스택 프로그램을 종료합니다 ==========')
        break