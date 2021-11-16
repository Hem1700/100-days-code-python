# Local and Global Variable

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()


# Global Scope 
player_health = 10
def player():
    print(player_health)

player()


# There is no block scope

game_level = 3
enemies = ['Skeleton', 'Zombie', 'Alien']
if game_level < 5:
    new_enemy = enemies[0]


print(new_enemy)