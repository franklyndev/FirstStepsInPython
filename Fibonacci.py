n1 = 0
n2 = 1
n3 = 0
c = 1
termos = int(input("Quantos termos você deseja: "))
print(n1,"", end = "")
while c < termos:
    if n1 <= n2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(f"{n1} ", end = "")
    c += 1