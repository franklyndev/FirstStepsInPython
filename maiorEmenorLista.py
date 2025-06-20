valores = []
big = 0
small = 0
for i in range(0, 5):
    valores.append(int(input("Enter a number: ")))
    if i == 0:
        big = small = valores[i]
    else:
        if valores[i] > big:
            big = valores[i]
        if valores[i] < small:
            small = valores[i]   
print(valores)    
print(f"The max value: {big}, entered in the positions ", end = "")
for c, v in enumerate(valores):
    if big == v:
        print(f"{c}...")
print(f"The min value: {small}, entered in the positions ", end = "")
for c, v in enumerate(valores):
    if small == v: 
        print(f"{c}...", end = "")