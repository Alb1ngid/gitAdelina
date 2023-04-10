
class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.named = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def __str__(self):
        return f'Name: {self.named}\n' \
               f'Nikname: {self.nickname}\n' \
               f'Superpower: {self.superpower}\n' \
               f'Health points: {self.health_points}\n' \
               f'Catch phrase: {self.catchphrase}'

    def get_name(self):
        print(f'Get name: {self.named}')

    def get_healht(self):
        return f'Health * 2: {self.health_points * 2}'

    def __len__(self):
        return f'Lenth of catch phrase: {len(self.catchphrase)}'

people1 = SuperHero('Тор', 'Повелитель молнии','Молот и гром', 500, 'Хаймдалл! Открой радужный мост!')


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
          super().__init__(name, nickname, superpower, health_points, catchphrase)
          self.damage = damage
          self.fly = fly

    def get_healht(self):
          self.fly = True
          return self.health_points ** 2

    def __str__(self):
          print('fly in the True_phrase')

earth_hero = EarthHero('Ivan Goncharov', 'Haed Chamberlain', 'The precipice', 2700, "God is gracious", 1000)

class AirHero(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def get_healht(self):
        self.fly = True
        return self.health_points ** 2

    def __str__(self):
        print('fly in the True_phrase')

air_hero = AirHero('Yuno', 'Meal-Saving Prince', 'Wind magic', 2550, "I'm not givving up", 1000)

class Villain(AirHero):

    def init(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        AirHero.__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        SuperHero.people = 'monster'

    def gen_X(self):
        pass

    def crit(self):
        return self.damage ** 2

villain = Villain('Бэтмен', 'bat', 'beast', 3500, "All heroes must to die!!!", 1500)

print(people1.get_name())
print(people1)
print(people1.__len__())
print(people1.get_healht())
print(villain.crit())
