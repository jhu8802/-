import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'input.txt')
txt = open(my_file,'r',encoding="euc-kr")
txt = txt.read().splitlines()

class sub:
    def __init__(self):
        self.library

    def add(self,text): #도서추가
        print("도서추가")
        add_book = str(input("도서명, 저자, 출판연도, 출판사명, 장르 입력")).splitlines()
        txt.extend(add_book)
    
    def search(self,text): # 검색
        print("도서검색")
        find = str(input("도서명, 저자, 출판연도, 출판사명, 장르 입력"))
        for i in range(0,len(txt)):
            if find in txt[i]:
                print(txt[i])

    def change(self,text): #수정
        print("도서수정")
        find2 = str(input("수정하고싶은 도서명, 저자, 출판연도, 출판사명, 장르 입력"))
        find3 = str(input("수정할내용의 도서명, 저자, 출판연도, 출판사명, 장르 입력"))
        for i in range(0,len(txt)):
            if find2 in txt[i]:
                txt[i] = find3
    
    def delete(self,text): #삭제
        print("도서삭제")
        find4 = str(input("수정하고싶은 도서명, 저자, 출판연도, 출판사명, 장르 입력"))
        for i in range(0,len(txt)):
            if find4 in txt[i]:
                txt.remove(txt[i])

    def show(self,text): #목록
        print("도서목록")
        for i in range(len(txt)):
            print(txt[i])

    def save(self,text): #저장
        print("도서저장")
        This_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_folder, 'input.txt')
        new = open(my_file, 'w',encoding='euc-kr')
        for i in range(len(txt)):
            new.writelines(' '.join(txt[i]))
            new.writelines('\n')
        new.close()

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
                self.add(text)
            elif (number == 2):
                self.search(text)
            elif (number == 3):
                self.change(text)
            elif (number == 4):
                self.delete(text)
            elif (number == 5):
                self.show(text)
            elif (number == 6):
                self.save(text)
            elif (number == 7):
                self.save(text)
                print("프로그램 종료")
                break
            else:
                print("제대로 입력 하세요")

a = sub()
a.library(txt)