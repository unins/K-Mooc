import pickle
import os
import time
import _script_run_utf8
_script_run_utf8.main()

BOOK_LIST_FILE = 'book_list_v00.pdb'

WORK_DIR = './_pickle/'
FILENAME_WITH_DIR = WORK_DIR + BOOK_LIST_FILE

class Library(object):
    def __init__(self, available_book_list):
        self.available_book_list = available_book_list

    def show_available_book_list(self):
        print('***현재, 대출 가능한 도서목록: ({}권)***'.format(len(self.available_book_list)))
        for i, book_title in enumerate(self.available_book_list, 1):
            print(' {:2}. {}'.format(i, book_title))

    def lend_book(self, book_title):
        if book_title in self.available_book_list:
            self.available_book_list.remove(book_title)
            print("*** '{}'책이 대출 되었습니다. ***".format(book_title))
        else:
            print("*** '{}'책은 현재 대출이 불가능 합니다. ***".format(book_title))

    def return_book(self, book_title):
        if book_title in self.available_book_list:
            print("*** '{}'책은 반납할 수 없습니다. ***".format(book_title))
        else:
            self.available_book_list.append(book_title)
            print("*** '{}'책이 반납 되었습니다. ***".format(book_title))

    def show_menu_selection(self):
        print('\n\n')
        print("*** 도서관 메뉴 리스트 ***")
        print(" 1. 대출가능 도서 목록 (Show)")
        print(" 2. 도서 대출하기 (Lend)")
        print(" 3. 도서 반납하기 (Return)")
        print(" 4. 나가기 (Quit)")
        return input('선택 메뉴: ')

class Student(object):
    def __init__(self, name):
        self.name = name
        print("*** '{}'님이 도서관에 접속하였습니다. ***".format(self.name))

    def student_lend_book(self):
        return input("대출 할 책 이름을 입력해 주십시오 : ")

    def student_return_book(self):
        while True:
            returned = input("반납 할 책 이름을 입력해 주십시오 : ").strip()
            if len(returned) == 0:
                print('잘못된 입력 입니다.')
                continue
            else:
                break
        return returned

def write_book_list_to_file(filename_with_dir, book_list):
    with open(filename_with_dir, 'w', encoding='utf8') as f:
        book_titles = ""
        for book_title in book_list:
            book_titles += book_title + '\n'
        f.write(book_titles)

def read_book_list_from_file(filename_with_dir):
    if not os.path.isfile(filename_with_dir):
        book_list = [
            '도라에몽',
            '나루토',
            '공각기동대',
            '포켓몬스터',
            '영미 컬링 성공 비법']
        return book_list
    else:
        with open(filename_with_dir, 'r', encoding='utf8') as f:
            book_list = f.read().strip().split('\n')
            return book_list

BOOK_LIST = read_book_list_from_file(FILENAME_WITH_DIR)
lib = Library(BOOK_LIST)
st1 = Student('박성하')

choice = lib.show_menu_selection()
while True:
    if choice == '1':
        os.system('cls')
        lib.show_available_book_list()
        choice = lib.show_menu_selection()
        continue
    elif choice == '2':
        os.system('cls')
        lib.lend_book(st1.student_lend_book())
        choice = lib.show_menu_selection()
        continue
    elif choice == '3':
        os.system('cls')
        lib.return_book(st1.student_return_book())
        choice = lib.show_menu_selection()
        continue
    else:
        os.system('cls')
        write_book_list_to_file(FILENAME_WITH_DIR, BOOK_LIST)
        good_bye = "이용해 주셔서 감사합니다."
        for i in range(len(good_bye)):
            print(good_bye[i], end='', flush=True)
            time.sleep(0.1)
        time.sleep(1)
        break
