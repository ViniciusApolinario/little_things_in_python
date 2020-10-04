preco= float(input("Valor do produto: R$"))
qtdd= int(input("quantidade: "))
print("Formas de pagamento : 1-Dinheiro , 2-Boleto , 3-Cartão")
forma = int(input("Escolha uma forma (1,2 ou 3): "))

total=preco*qtdd

if forma== 1:
    subtotal = total-(0.15*total)
    economia = total - subtotal
elif forma==2:
    subtotal = total-(0.10*total)
    economia = total - subtotal
elif forma==3:
    v = int(input("Em quantas vezes ? : "))
    if v==1:
        subtotal = total-(0.05*total)
        economia = total - subtotal
    else :
        subtotal = (total-(0.05*total))-(0.02*(total-(0.05*total)))
        economia = total - subtotal

print(" O valor da sua compra foi de R$" + f"{subtotal:.2f}" + "! Voce economizou R$" + f"{economia:.2f}") 

