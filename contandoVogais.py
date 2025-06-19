vogais = ("Aviao", "Agua", "Terra", "Fogo", "Vento")
for i in vogais:
    print(f"\nA palavra {i} tem ", end="")
    for palavra in i:
        if palavra.lower() in "aeiou":
            print(palavra , end="")