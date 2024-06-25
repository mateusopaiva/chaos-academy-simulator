class Gym:
    def __init__(self):
        self.dumbbells = [i for i in range(10, 36) if i % 2 == 0]
        self.dumbbell_rack = {}
        self.reset_day()

    def reset_day(self):
        self.dumbbell_rack = {i:i for i in self.dumbbells}

    def list_dumbbells(self):
        return [i for i in self.dumbbell_rack.values() if i != 0]

    def list_empty_slots(self):
        return [i for i in self.dumbbell_rack if self.dumbbell_rack[i] == 0]
    
    def pick_dumbbell(self, weight):
        if weight not in self.dumbbell_rack.values():
            raise ValueError("Peso não encontrado.")
        halt_pos = list(self.dumbbell_rack.values()).index(weight)
        key_halt = list(self.dumbbell_rack.keys())[halt_pos]
        self.dumbbell_rack[key_halt] = 0
        return weight

    def return_dumbbell(self, pos, weight):
        self.dumbbell_rack[pos] = weight

    def calculate_chaos(self):
        chaos_num = [i for i, j in self.dumbbell_rack.items() if i != j]
        return len(chaos_num) / len(self.dumbbell_rack)
