import random

class User:
    def __init__(self, type, gym):
        self.type = type
        self.gym = gym
        self.weight = 0

    def start_workout(self):
        weight_list = self.gym.list_dumbbells()
        self.weight = random.choice(weight_list)
        self.gym.pick_dumbbell(self.weight)

    def end_workout(self):
        empty_slots = self.gym.list_empty_slots()
        if self.type == 1 and self.weight in empty_slots:
            self.gym.return_dumbbell(self.weight, self.weight)
        else:
            pos = random.choice(empty_slots)
            self.gym.return_dumbbell(pos, self.weight)
        self.weight = 0

