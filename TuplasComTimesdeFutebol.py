times = ("Bahia", "BotaFogo", "Ceará", "Chapecoense", "Corinthians", "Cruzeiro", "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Atlético-MG", "Internacional", "Juventude", "Mirassol", "Palmeiras", "Santos", "São Paulo", "Vasco da Gama", "Vitória", "Sport")
print("-="*15)
print(f"Times brasileirão\n{times}")
print("-="*15)
# Usando : consigo usar um intervalo entre um ponto de incio escolhido e um fim
print(f"5 primeiros times: {times[0:5]}")
print("-="*15)
# A partir do momento que eu ponho o indice negativo, eu inverto a ordem
print(f"Os últimos 4 colocados: {times[-4:]}")
print("-="*15)
# Sorted usado para organizar os valores em ordem 
print(f"Times em ordem alfabética {sorted(times)}")
print("-="*15)
# Index usado para encontrar a posição de algum valor em uma tupla
print(f"Posição da Chapecoense: {times.index("Chapecoense")}")
print("-="*15)

