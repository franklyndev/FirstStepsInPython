print("--------------------")

print("       Point        ")
print("--------------------")
name = input("What's your name: ")
perfil = input("What's your acess perfil: ")
day = input("What's the day of week: ")
hour = int(input("What time's it: "))

acess = False
justify = ""

print("-------------")
print(f"Name: {name}")
print(f"Perfil: {perfil}")
print(f"Day: {day}")
print(f"Hour: {hour}")
print("-------------")

if perfil == "adm":
    acess = True
    justify = "Total acess released"
elif perfil == "financial":
    if 8 <= hour <= 18:
        acess = True
        justify = "Total acess released in allowed time(8:00 - 18:00)" 
    else:
        justify = "Acess denied"
elif perfil == "technical":
    if day == "sunday":
        justify = "You can't work today"
    elif 6 <= hour <= 22:
        acess = True
        justify = "Acess released in allowed time(6:00 - 22:00)"
    else:
        justify = "Acess denied"
else:
    justify = "Invalid Perfil"

print(f"Acess: {acess}")
print(f"justify: {justify}")
print("----------------------")