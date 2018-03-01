""" 클래스 오브젝트 : (객체 지향 프로그래밍 - OOP: Obj. Oriented Progmng)
   ** 함수형 프로그래밍 / 객체지향 프로그래밍 = 파이썬 특징의 2축!

  1.클래스명 작명 = 파스칼 케이스 (ThisIsPascalCase)
  - 클래스 함수(매서드)의 첫번째 인자 = 인스턴스 자신(Self)
  - 클래스간 띄어쓰기는 2칸 / 함수(매서드)는 1칸 이다.

  2.오브젝트(객체) : 클래스 오브젝트 <--> 인스턴스
  - 값 (field) = 클래스변수 or 인스턴스 변수
  - 기능 (method) = 매서드, 매직매서드, 더블언더스코어

  3.클래스만의 매우 특별한 기능
   * 상속 (Inherit) = 부모(Parent) - 자식(Child)
   * 중복 (Override) = 덮어쓰기 / 겹쳐쓰기
 """
import _script_run_utf8
_script_run_utf8.main()


class ManOne(object):
    icon = '성격이 더러운'

    def __init__(self, name, age):
        """생성자: 객체가 생성되면 제일 먼저 실행되는 매서드"""
        self.name = name
        self.age = age
        self.__my_secret = '말할 수 없는 비밀'

    def say_hello(self, other_instance):
        print('{}({}):안녕하세요, {}({})씨'.format(
            self.name, self.age, other_instance.name, other_instance.age))

    def __add__(self, other_instance):
        print("{}와{}가 겨론하다...".format(self.name, other_instance.name))

    def __sub__(self, other_instance):
        print("{}와{}가 잏온하다...".format(self.name, other_instance.name))

    def __del__(self):
        print("{}.. 외롭게 죽다..".format(self.name))

    def show_shortened_life_story_with(self, other_instance):
        print("--------------------\n"
              "{}, {}의 인생스토리: 서사시\n"
              "--------------------".format(self.name, other_instance.name))
        self + other_instance
        self - other_instance
        self.__del__()

    """ 클래스 매서드는, 인스턴스 명으로 클래스변수에 접근할 방법을 열어준다."""
    @classmethod
    def set_icon_change(cls, modified_string):
        cls.icon = modified_string

    """ 스테틱 매서드는, 객체기능과 상관없지만 그림(편의)상 포함시켜야 할 때"""
    @staticmethod
    def shown_shortened_life_story_with(obj1, obj2):  # 상관없으니 'self'인자 없음
        print("\n\n'{}'와 '{}'의 짧은 인생스토리~ 시작!!.."
              '\n--------------------'.format(obj1.name, obj2.name))
        obj1 + obj2
        obj1 - obj2
        obj1.__del__()
        print('\n\n')

    @staticmethod
    def show_secret_of(instance):
        """ 여기서,  질문~!!
        .. 성격을 알아보는 기능은 어느 객체의 것일까? = 공통기능 (바깥에 정의)
        (또는 스테틱 매서드로, 그냥 그림(편의)상 포함만 시켜 놓을 수 있다.)
        """
        print("{}의 성격은... {}".format(instance.name, instance.icon))

    """ 클래스 매서드는, 인스턴스 명으로 클래스변수에 접근할 방법을 열어준다.(나중에)"""
    @classmethod
    def set_icon_change(cls, modified_string):
        cls.icon = modified_string

    """ 스테틱 매서드는, 객체기능과 상관없지만 그림(편의)상 포함시켜야 할 때(나중에)"""
    @staticmethod
    def show_shortened_life_story_with(obj1, obj2): # 상관없으니 'self'인자 없음
        print("\n\n'{}'와 '{}'의 짧은 인생스토리~ 시작!!.."
            '\n--------------------'.format(obj1.name, obj2.name))
        obj1 + obj2
        obj1 - obj2
        obj1.__del__()

    # 프라이빗 메서드는 인스턴스로는 보이지 않는다. = 클래스로 호출한다.
    def __dont_use_by_anyone(self):
        print("*** 접근을 거부한다. ***")


class ManTwo(ManOne):
    icon = '성격이 좋은'

    def say_thankyou(self, other_instance):
        print('{}{}{}{}{}{}{}{}{}'.format(self.name, '(', self.age, '):',
                                          '정말 ', '더럽게 ', '고맙네요 ', other_instance.name, '씨'))


"""객체 선언/생성 : mo = 인스턴스 <--> 오브젝트 = 클래스 객체"""
mo = ManOne('철수', 24)
mt = ManTwo('영희', 17)


ManOne.icon = '성격이 드러운'

m1 = ManOne('주나', 15)
m2 = ManOne('준아', 15)

m1.icon = '성격이 없는'
for instance in [mo, mt, m1, m2]:
    instance.show_secret_of(instance)

print(
    """
    ▨▨▨
  ▨    ▨▨
▨▨      ▨▨
▨▨      ▨▨
▨▨      ▨▨
  ▨▨    ▨
    ▨▨▨
"""
)

mo.say_hello(mt)
mt.say_thankyou(mo)
# mo.show_shortened_life_story_with(mt)

# @staticmethod를 호출할때는 객체 상관없지만, 인스턴스의 이름으로 호출한다.
mo.shown_shortened_life_story_with(mo, mt)

""" 프라이빗 매서드(더블언더스코어)를 호출하는 방법
  - 파이썬은 기본적으로 '퍼블릭'이다... 가정: 양식이 있는, 다 큰 어른이 뭘 숨기나?
  - '더블언더스코어'는 '맹글링' 목적도 있다. (동일이름의 중복 매서드 구분)
    # 'ManOne' object has no attribute '__dont_use_by_anyone'
    # m1.__dont_use_by_anyone()        # 안된다...!!
    # ManOne.__dont_use_by_anyone()    # 안된다니까... ?!!
"""
m1._ManOne__dont_use_by_anyone()
print(m1._ManOne__my_secret)
