class Riven:
    camp= ''
    def __init__(self,nickname,aggressivity=54,live_value=414,money=1000,armor=3):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.live_value = live_value
        self.money =money
        self.armor = armor

    def attack(self,enemy):
        damage_value = self.aggressivity-enemy.armor
        enemy.life_value -=damage_value


class Garen:
    camp='Demacia'
    def __init__(self,nickname,
                 aggressivity=58,
                 life_value=455,
                 money=100,
                 armor=10):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
        self.armor=armor
    def attack(self,enemy):
        damage_value=self.aggressivity-enemy.armor
        enemy.life_value-=damage_value


class BlackCleaver:
    def __init__(self,price=475,aggrev=9,life_value=100):
        self.price=price
        self.aggrev=aggrev
        self.life_value=life_value
    def update(self,obj):
        obj.money-=self.price #减钱
        obj.aggressivity+=self.aggrev #加攻击
        obj.life_value+=self.life_value #加生命值
    def fire(self,obj): #这是该装备的主动技能,喷火,烧死对方
        obj.life_value-=1000 #假设火烧的攻击力是1000


r1 = Riven('徐')
g1 = Garen('盖')

