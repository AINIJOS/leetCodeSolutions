class Lina():
    def __init__(self, health=600, mana=435, armor=3.68, damage=57, movespeed=290, attackspeed=0.77):
        self.health = health
        self.mana = mana
        self.armor = armor
        self.damage = damage
        self.moveSpeed = movespeed
        self.attackSpeed = attackspeed

    def dragonSlave(self, mana=100, damage=85):
        if self.mana < mana:
            print('Not enough mana!!!')
        else:
            self.mana -= mana
            self.damage += damage
            print("Lina научилась управлять огненным дыханием дракона пустынь.")
        self.FierySoul()

    def LightStrikeArray(self, mana=100, damage=80):
        if self.mana < mana:
            print('Not enough mana!!!')
        else:
            self.mana -= mana
            self.damage += damage
            print("Lina управляет энергией Солнца, заставляя воздух воспламеняться по ее воле.")
        self.FierySoul()

    def FierySoul(self, movespeed=0.05, attackspeed=4):
        self.moveSpeed += movespeed * self.moveSpeed
        self.attackSpeed += attackspeed

    def LagunaBlade(self, mana=250, damage=500):
        if self.mana < mana:
            print('Not enough mana!!!')
        else:
            self.mana -= mana
            self.damage += damage
            print("Воздух вокруг Lina становится таким горячим, что он обжигает молнией любого врага")
        self.FierySoul()


    def stats(self):
        print("healh:", self.health, "Mana:" ,self.mana,"Armor:", self.armor,"Damage:" , self.damage,"Move Speed:" , self.moveSpeed,"Attack Speed:", self.attackSpeed)


lina = Lina()
lina.stats()

lina.LagunaBlade()
lina.LightStrikeArray()
lina.dragonSlave()

lina.stats()
