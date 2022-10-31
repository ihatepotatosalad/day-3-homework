class Podracer():
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        if self.condition == "perfect":
            print('does not need ot be fixed')
        else:
            print('repairing')
            self.condition = 'repaired'


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        print('vroom')
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        print('vroooom')
        self.condition = 'trashed'


pot1 = SebulbasPod(8, 'perfect', 8.99)

pot1.flame_jet()
print(pot1.condition)
pot1.repair()
print(pot1.condition)
