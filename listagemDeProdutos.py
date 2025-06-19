listagem = ("Lápis", 1.50,
            "Borracha", 2.00,
            "Apontador", 3.00,
            "Canetas", 2,
            "Mochila", 110,
            "Livro", 20,
            )
print("-" * 40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print("-" * 40)
for position in range(0, len(listagem)):
    if position % 2 == 0:
        print(f"{listagem[position]:.<30}", end= "")
    else:
        print(f"R$ {listagem[position]:.2f}")    