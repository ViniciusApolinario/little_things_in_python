want = True
count=0
while want==True :
    inp = input("Quer digitar um numero ? (Y or N): ")
    if inp=="y" or inp=="Y":
        number = input("Digite:")
        print(number)
        count=count+1
    else :
        want = False
        print("ok")
        print("voce inseriu " + str(count) + " vezes") 
