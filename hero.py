
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

print(people1.get_name())
print(people1)
print(people1.__len__())
print(people1.get_healht())