import math

cat_op = int(input("Digite o número do cateto oposto: "))
cat_ad = int(input("Digite o número do cateto adjacente: "))
hipotenusa = cat_op**2 + cat_ad**2
print("{:.2f}".format(math.sqrt(hipotenusa)))