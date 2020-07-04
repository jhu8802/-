import os
import sublibrary

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'input.txt')
txt = open(my_file,'r',encoding="euc-kr")
txt = txt.read().splitlines()

class good:
    def __init__(self):
        self.a = sublibrary.sub()


    def library(self,text):
        while(True):
            print("=====menu=====")
            print('1.도서 추가')
            print('2.도서 검색')
            print('3.도서 정보 수정')
            print('4.도서 삭제')
            print('5.도서 출력')
            print('6.도서 저장')
            print('7.도서 종료(자동 저장)')

            number = int(input("선택하세요"))
            if (number == 1):
                self.a.add(text)
            elif (number == 2):
                self.a.search(text)
            elif (number == 3):
                self.a.change(text)
            elif (number == 4):
                self.a.delete(text)
            elif (number == 5):
                self.a.show(text)
            elif (number == 6):
                self.a.save(text)
            elif (number == 7):
                self.a.save(text)
                print("프로그램 종료")
                break
            else:
                print("=====제대로 입력 하세요=====")
                self.library(text)

a = good()
a.library(txt)