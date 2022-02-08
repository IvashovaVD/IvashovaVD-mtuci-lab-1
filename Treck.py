# IvashovaVD-mtuci-lab-1
GROWTH = 160
WEIGHT = 160
STEPS = 60
ACTIVITY = 30
len = GROWTH/4+0.37
len = STEPS/len
distance = 0.035*WEIGHT+(len**2/GROWTH)*0.029*WEIGHT
print(f"Калорий сожено:{len}; Пройдено:{distance}")
if distance < 2:
    print('Меньше 2х км')
elif distance < 4:
    print('Меньше 4х км')
if distance > 4:
    print('Больше 4х км')GROWTH = 160



#Калорий сожено:1.4862521674510776; Пройдено:5.664059419652339
#Больше 4х км
