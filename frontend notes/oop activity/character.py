class Character():
    def __init__(self, real_name):
        self.name=real_name
                
    def set_hero_name(self, hero_name):
            self.hero_name=hero_name

    def set_power(self, power):
            self.power = power
            
    def get_hero_name(self):
                print(self.hero_name)

    def get_power(self):
                print(self.power)
