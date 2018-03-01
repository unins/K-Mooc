"""도서관 객체와 학생 객체들의 상호작용"""
import os
import time

DECORATOR = "=+" * 20 + "="

class Library(object):
    BOOK_LIST_DICT = {
        1: ['k-001', '원주율 하루만에 1000자리 외우기'],
        2: ['k-002', '피카소처럼 그리기'],
        3: ['k-003', '더티밤 갓겜론'],
        4: ['k-004', '한국 중심 세계사'],
        5: ['k-005', '수능 컨닝법 101 가지'],
        6: ['k-006', '영미 컬링 성공 비법'],
        7: ['k-007', '존 윅이 말하는 좋은 총 구별 법'],
    }
    def __init__(self):
        print("\n도서관 시스템에 접속하신 것을 환영합니다.\n\n")

    def get_show_system_menu(self):
        while True:
            print(DECORATOR,
                '\n\t번호를 선택해 주십시오.',
                '\n-------------------------------------',
                '\n\t1.책 리스트 보기'
                '\n\t2.책 대출하기'
                '\n\t3.책 반납하기'
                '\n\t4.종료하기'
                '\n-------------------------------------'
                )
            choice = int(input().strip()[:1])
            if not 1 <= choice <= 4:
                os.system('cls')
                print('************ ERROR ************\
                    \n-------------------------------\
                    \n        INPUT NUMBER IS\
                    \n        NOT IN THE LIST\
                    \n-------------------------------')
                time.sleep(3)
                os.system('cls')
                continue
            else:
                return choice

    def give_book_change_list(self, other_obj, dict_key):
        print(DECORATOR,
            '\n{}님에게 "[{}]{}" 의 대출 허가를 하였습니다'.format(
            other_obj.name,
            self.BOOK_LIST_DICT[dict_key][0],
            self.BOOK_LIST_DICT[dict_key][1],
            ))
        del self.BOOK_LIST_DICT[dict_key]

class Student(object):
    HOME_LIST_DICT = {}

    def __init__(self, name):
        self.name = name
        pass

    def show_available_book_list(self, other_obj):
        pass

    def show_others_book_list(self, other_obj):
        print("%s님이 도서목록을 요청하였습니다.\n" %(self.name))
        print(DECORATOR + '\n'
            "\t대출 가능한 도서목록\n"
            "----------------------------------------")
        for key in other_obj.BOOK_LIST_DICT:
            print("{:2}. [{}]{}".format(
                key,
                other_obj.BOOK_LIST_DICT[key][0],
                other_obj.BOOK_LIST_DICT[key][1]))
        print("----------------------------------------")

    def get_borrow_book_dict_key(self, other_obj, dict_key):
        print(DECORATOR,
            '\n{}님이 "[{}]{}" 을(를) 대출 요청을 하였습니다'.format(
            self.name,
            other_obj.BOOK_LIST_DICT[dict_key][0],
            other_obj.BOOK_LIST_DICT[dict_key][1],
            ))
        self.HOME_LIST_DICT[len(self.HOME_LIST_DICT) + 1] = [
            other_obj.BOOK_LIST_DICT[dict_key][0],
            other_obj.BOOK_LIST_DICT[dict_key][1],
        ]
        return dict_key

lb = Library()
st1 = Student('박성하')

menu_select = lb.get_show_system_menu()

while True:
    if menu_select == 1:
        os.system('cls')
        st1.show_others_book_list(lb)
        menu_select = lb.get_show_system_menu()
    elif menu_select == 2:
        os.system('cls')
        book_request = input()
        dict_key = st1.get_borrow_book_dict_key(lb, 2)
        lb.give_book_change_list(st1, dict_key)
        menu_select = lb.get_show_system_menu()
        pass
    elif menu_select == 3:
        pass
    else:
        os.system('cls')
        print('이용해 주셔서 감사합니다.')
        break
