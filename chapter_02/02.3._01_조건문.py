신장 = 170
체중 = 82
BMI = 체중 / ((신장/100)**2)
print(BMI)

if BMI > 30:
    print("당신은 비만입니다.")
elif BMI > 25:
    print("당신은 과체중입니다.")
else:
    print("당신은 정상체중입니다.")