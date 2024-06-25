import random
from gym import Gym
from user import User

def main():
  print("Simulação de Academia: Uso de Halteres por Usuários\n")
    
  num_organized = int(input("Digite o número de usuários organizados (tipo 1): "))
  num_disorganized = int(input("Digite o número de usuários desorganizados (tipo 2): "))
  num_days = int(input("Digite o número de dias para a simulação: "))

  gym = Gym()

  print(f"\nCriando {num_organized} usuários organizados (tipo 1) e {num_disorganized} usuários desorganizados (tipo 2)...\n")
  users = [User(1, gym) for _ in range(num_organized)]
  users += [User(2, gym) for _ in range(num_disorganized)]
  random.shuffle(users)

  chaos_levels = []

  for day in range(1, num_days + 1):
    print(f"\n--- Dia {day} ---")
    gym.reset_day()
    random.shuffle(users)
        
    for user in users:
      user.start_workout()
    for user in users:
      user.end_workout()
    
    print("Estado final do porta-halteres:")
    for pos, weight in gym.dumbbell_rack.items():
        print(f"Posição {pos}: Haltere de {weight} kg")

    chaos_level = gym.calculate_chaos()
    chaos_levels.append(chaos_level)
    print(f"Nível de caos: {chaos_level:.2%}")
  
  average_chaos = sum(chaos_levels) / len(chaos_levels)
  print(f"\nMédia de nível de caos ao longo dos {num_days} dias: {average_chaos:.2%}")

  input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()
