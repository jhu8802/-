import sys

class Train:
    def __init__(self):
        self.line = []
        self.now = []
        self.seat_train = []
        self.seat_change = []

    def memo(self):
        self.Train_List = open("/Users/janghyeon-u/Desktop/hiii/-/기차/TrainList.txt", 'r', encoding='euc-kr')
        self.line = self.Train_List.read().splitlines()
        del self.line[0]
        self.Train_List.close()
        return self.line

    def menu(self):
        while True:
            print("-------메뉴-------")
            print("1. 빠른시간 기차 검색 및 예매")
            print("2. 전체 기차 리스트 출력")
            print("3. 나의 예매 현황 출력 및 예매 취소")
            print("4. 프로그램 종료")

            choice = int(input("메뉴를 입력해주세요 : "))

            if choice == 1:
                self.reser()
            elif choice == 2:
                self.time_table()
            elif choice == 3:
                self.cancel()
            elif choice == 4:
                print(" 프로그램 종료하겠습니다.")
                self.end()
                break
            else:
                print ("메뉴에 있는 번호를 입력하시오.")
                self.menu()       
        
    def info(self):
        self.want = input("찾으시는 시간, 출발역, 도착역, 열차종류를 입력하세요 \n").split()
        self.want[0] = list(map(int,self.want[0]))
        return self.want
    
    def program(self):
        if not self.now:
            self.memo()
        self.info()
        self.time2 = []
        self.time3 = []
        self.Train_List = open("/Users/janghyeon-u/Desktop/hiii/-/기차/TrainList.txt", 'r', encoding='euc-kr')
        self.time_diff = []
        self.start = []
        self.end = []

        while True:
            time = self.Train_List.readline()
            
            replace = time.replace(":","")
            a = replace.replace("\n","")
            if time:
                self.time2.append(a[0:4])
                self.time3.append(a[-2:])
                self.seat_change.append(time[0:-3])
                self.start.append(a[5:8].strip())
                self.end.append(a[11:14].strip())
            else:
                break  
        del self.time2[0], self.time3[0],self.start[0],self.end[0]
        
        self.Train_List.close()
        for j in range(len(self.line)):
            self.time2[j] = list(map(int,self.time2[j]))
        if not self.seat_train:
            self.seat_train = list(map(int,self.time3))

        for k in range(len(self.line)):
            self.time_diff.append(600*(self.time2[k][0] - self.want[0][0]) + 60*(self.time2[k][1] - self.want[0][1]) + 10*(self.time2[k][2] - self.want[0][2]) + (self.time2[k][3] - self.want[0][3]))
            if self.time_diff[k] < 0:
                self.time_diff[k] = sys.maxsize

        return self.time_diff

    def reser(self): #기차 검색 및 예매
        self.program()
        self.near = []
        
        for i in range(len(self.time_diff)):
            if (self.want[1] == self.start[i]) and (self.want[2] == self.end[i]) is True:
                    if self.time_diff[i] == min(self.time_diff):
                        self.near.append(self.line[i])        

        if not self.near: 
            print ("잘못 입력 하셨습니다.")
            self.info()
        for m in range(len(self.near)):
            print (m,".",self.near[m])
            if m == (len(self.near)-1):
                print (m+1,".","뒤로가기")         
        
        try: 
            answer = int(input("예매하시겠습니까 ? : "))
        except TypeError:
            print ("잘못 입력 하셨습니다.") 
            self.reser()

        if answer > len(self.near) or answer < 0:
            print("목록에 없습니다.")
            self.reser()
        elif answer == len(self.near):
            self.menu()
        else:
            for i in range(len(self.line)):
                if self.line[i] == self.near[answer]:
                    if self.seat_train[i] == 0:
                        print ("매진 입니다.")
                    else:    
                        self.seat_train[i] = self.seat_train[i] - 1
                        self.line[i] = self.seat_change[i+1] + str(self.seat_train[i])
                        self.now.append(self.line[i])
                        print ("[ {0} ]이 예매 되었습니다.".format(self.line[i])) 
        
        return self.line, self.now, self.seat_train, self.seat_change

    def time_table(self): #전체 기차 시간표 출력
        if not self.line:
            self.memo()
            for i in range(len(self.line)):
                print (self.line[i])
        else:
            for i in range(len(self.line)):
                print (self.line[i])
                  
    def cancel(self): #예매 현황 출력 및 취소
        print ("1. 예매 내역 ")
        print ("2. 예매 내역 취소 (선입선출)")
        print ("3. 뒤로가기 ")
        
        cancel_input = int(input("입력하세요"))
        if cancel_input == 1:
            print (self.now)
            if not self.now:
                print ("예매된 내역이 없습니다.")
            return self.now
            
        elif cancel_input == 2:
            if self.now:
                for i in range(len(self.line)):
                    if self.now[0] == self.line[i]:
                        self.seat_train[i] = self.seat_train[i] + 1
                        self.line[i] = self.seat_change[i+1] + str(self.seat_train[i])
                print("[ {0} ]가 예매 취소 되었습니다.".format(self.now[0]))
                self.now.pop(0)

            elif not self.now:
                print ("예매 된 내역이 없습니다.")
                self.menu()
        elif cancel_input == 3:
            self.menu()
        else:
            print ("다시 입력해주세요 : ")
            self.cancel()
        return self.line, self.now, self.seat_train, self.seat_change
    
    def end(self): #프로그램 종료
        sys.exit()
                  
if __name__ == "__main__":                    
    korail = Train()
    print (korail.menu())