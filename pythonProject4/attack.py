import random
from classes.enemy import  Enemy

enemy1 = Enemy(200,60)
print('Hp: ',enemy1.get_hp())

enemy2 = Enemy(75,90)

'''
playerhp = 260
ennemyatkl = 60
ennemyatkh = 80

while playerhp > 0:
    dmg = random.randrange( ennemyatkl, ennemyatkh)
    playerhp -= dmg

    if playerhp <= 30:
        playerhp = 30

    print('Ennemy strikes for',dmg,'points of damage. Current HP is ', playerhp)

    if playerhp > 30:
        continue

    print("You have low health. You've been teleported to the nearest inn")
    break
'''