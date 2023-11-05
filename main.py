from Character import Character
from ninja import Ninja

player1 = Character(name='Петя', health=100,
                    damage=10, defence=0)
player2 = Ninja(name='Вася', health=120,
                    damage=20, defence=0)

print(player1)
print(player2)

for _ in range(3):
    player1_dmg = player1.attack(player2)
    player2_dmg = player2.attack(player1)

    print(f'{player1.name} атаковал {player2.name} и нанёс {player1_dmg} урона.')
    print(f'У {player2.name} осталось {player2.health} здоровья.')
    print(f'{player2.name} атаковал {player1.name} и нанёс {player2_dmg} урона.')
    print(f'У {player1.name} осталось {player1.health} здоровья.')
    print()

print(player1)
print(player2)
