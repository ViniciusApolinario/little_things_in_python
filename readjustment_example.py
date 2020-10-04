nome = input("insira seu nome : ")
cepefe = input("insira CPF (apenas numeros): ")
sal = input("Insira o Salario(use pontos ao inves de virugulas) : R$")
reajuste = ""
salario_inicial = ""

#bloco só pra nao dar erro feio , ignorar
try :
    cpf = int(cepefe)
    salario = float(sal)
    salario_inicial = sal
    
except ValueError:
        print("INSIRA APENAS NUMEROS NO CPF !!!!!!")
        print("Use pontos ao inves de virgulas no salario")
#bloco só para nao dar erro feio , ignorar

if salario<=1500:
    reajuste = "7%"
    salario = salario + (0.07*salario)
    dif = salario-float(salario_inicial)
elif salario<=2000 and salario > 1500:
    reajuste = "6%"
    salario = salario + (0.06*salario)
    dif = salario-float(salario_inicial)
elif salario<=3000 and salario > 2000:
    reajuste = "5%"
    salario = salario + (0.05*salario)
    dif = salario-float(salario_inicial)
elif salario > 3000:
    reajuste = "4%"
    salario = salario + (0.04*salario)
    dif = salario-float(salario_inicial)
    
print("-------------")
print("Colaborador :" + nome);
print("salario incial :R$" + salario_inicial);
print("Reajuste :" + reajuste);
print("Valor de reajuste :R$" + str(dif));
print("salario atual :R$" + str(salario));


