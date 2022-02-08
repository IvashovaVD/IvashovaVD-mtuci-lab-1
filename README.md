# IvashovaVD-mtuci-lab-1
rost=160
ves=160
kolSh=60
vac=30
v=rost/4+0.37
v=kolSh/v
rs=0.035*ves+(v**2/rost)*0.029*ves
print(f"Калорий сожено:{v}; Пройдено:{rs}")
