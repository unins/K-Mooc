class Interagent(object):


    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.group, self.location = "국제첩보", "모름"
        self.secret = "알수없음"
        self.inven_dict = {
            1: ['권총', 1],
        }

    def show_introduction(self):
        print("{} in {}\n----------------".format(self.group, self.location))
        print("*** {}({}) ***".format(self.name, self.age))
        print(self.secret)

        print("=== INVENTORY ===")
        for key in self.inven_dict:
            print("{}. {} = {}".format(
                key, self.inven_dict[key][0], self.inven_dict[key][1]))
        print('\n\n')

    def say_hello(self, other_object):
        print("{}({}):넌 죽었어, {}!".format(
            self.name,
            self.group,
            other_object.name))

    def reveal_secret(self, other_object):
        print("{}({}): 네놈의 비밀이 '{}'인 것을 나는 이미 알고있다, {}.".format(
            self.name,
            self.group,
            other_object.secret,
            other_object.name))

class KingsMan(Interagent):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.group, self.location = "킹스맨", "런던/영국"
        self.secret = "본래 재단사이다"
        self.inven_dict = {
            1: ['우산', 1],
            2: ['구두 칼', 2],
        }

    def say_hello(self, other_object):
        print("{}({}): 매너가, 사람을, 만든다. 그게 무슨 뜻인지 아나, {}?".format(
            self.name,
            self.group,
            other_object.name))


class StatesMan(KingsMan):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.group, self.location = "스테이츠맨", "텍사스/미국"
        self.secret = "술주정뱅이"
        self.inven_dict = {
            1: ['술', 3],
            2: ['채찍', 1],
            3: ['리볼버', 2],
        }


class MercServ(Interagent):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.group, self.location = "용병서비스", "런던/영국"
        self.secret = "돈에 눈이 멀었다"
        self.inven_dict = {
            1: ['돌격소총', 1],
            2: ['권총', 1],
            3: ['칼', 1],
        }


ia = Interagent("Dik Rokhard", 34)
ia2 = Interagent("James Bond", 35)
km = KingsMan("Mans King", 27)
sm = StatesMan("Vodka", 36)
ms = MercServ("Sky Hammer", 38)
ia.secret = "몸이 딱딱해서 총알이 안통한다(?)"
ia2.secret = "약점이 없다"


for agent in [ia, km, sm, ms]:
    agent.show_introduction()

ms.say_hello(km)
km.say_hello(ms)
ms.reveal_secret(km)
km.reveal_secret(ia)
km.reveal_secret(ia2)
