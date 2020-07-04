import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'input.txt')
txt = open(my_file,'r',encoding="euc-kr")
txt = txt.read().splitlines()

class sub:
    def __init__(self):
        self.library = []

    def add(self,text): #도서추가
        print("도서추가")
        add_book = str(input("도서명, 저자, 출판연도, 출판사명, 장르 입력\n")).splitlines()
        txt.extend(add_book)
        print("{0}이 추가 되었습니다.".format(add_book))
    
    def search(self,text): # 검색
        print("도서검색")
        find = str(input("도서명, 저자, 출판연도, 출판사명, 장르 입력\n"))
        for i in range(0,len(txt)):
            if find in txt[i]:
                print("==============")
                print("{0}이 검색 되었습니다.".format(txt[i]))

    def change(self,text): #수정
        print("도서수정")
        find2 = str(input("수정하고싶은 도서명, 저자, 출판연도, 출판사명, 장르 입력\n"))
        find3 = str(input("수정할내용의 도서명, 저자, 출판연도, 출판사명, 장르 입력\n"))
        for i in range(0,len(txt)):
            if find2 in txt[i]:
                txt[i] = find3
                print("{0}으로 수정 되었습니다.".format(txt[i]))
    
    def delete(self,text): #삭제
        print("도서삭제")
        find4 = str(input("삭제하고싶은 도서명, 저자, 출판연도, 출판사명, 장르 입력\n"))
        for i in range(0,len(txt)):
            if find4 in txt[i]:
                print("{0}이 삭제 되었습니다.".format(txt[i]))
                del txt[i]
                
                

    def show(self,text): #목록
        print("=====도서목록=====")
        for i in range(len(txt)):
            print(txt[i])

    def save(self,text): #저장
        print("도서저장")
        This_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_folder, 'input.txt')
        new = open(my_file, 'w',encoding='euc-kr')
        for i in range(len(txt)):
            new.writelines(txt[i])
            new.writelines('\n')
        new.close()
        print("도서가 저장 되었습니다.")
