from collections import deque

firework_effects = deque(int(x) for x in input().split(',') if int(x) > 0)
explosive_powers = [int(x) for x in input().split(',') if int(x) > 0]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_powers:
    firework_effect = firework_effects.popleft()
    explosive_power = explosive_powers.pop()
    curent_sum = firework_effect + explosive_power

    if curent_sum % 3 == 0 and curent_sum % 5 == 0:
        crossette_firework += 1
    elif curent_sum % 3 == 0:
        palm_firework += 1
    elif curent_sum % 5 == 0:
        willow_firework += 1
    else:
        if firework_effect > 1:
            firework_effects.append(firework_effect - 1)
        explosive_powers.append(explosive_power)

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        break

if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if len(firework_effects) != 0:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if len(explosive_powers) != 0:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

print(f'Palm Fireworks: {palm_firework}')
print(f'Willow Fireworks: {willow_firework}')
print(f'Crossette Fireworks: {crossette_firework}')