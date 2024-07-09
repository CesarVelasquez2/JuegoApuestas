"Realizado por Cesar Velasquez, CI:30.398.706"

import random
while True:
    amount_play = 0
    counter_play = 0
    personal_acount = 0
    dice = 0

    while True:
        try:
            amount_play = int(input("Por favor, ingrese la apuesta con la que desea jugar. El minimo es de 5$.\n"))
            if(amount_play >= 5):
                break
            else:
                print("Monto incorrecto.")
        except ValueError:
            print("Valor erroneo ingresado. Solo se admiten numeros.")

    while True:
        counter_play += 1
        dice = random.randint(1,6)
        if(dice % 2 == 0):
            personal_acount += (amount_play * 2)
        else:
            personal_acount -= amount_play

        if(personal_acount >= 500):
            print("Has ganado.\nGanancia Final: " + str(personal_acount) +  "$.\nTotal de rondas jugadas: " + str(counter_play))
            break
        elif(personal_acount <= -100):
            print("Has perdido.\nDeuda Final: " + str(personal_acount) + "$.\nTotal de rondas jugadas: " + str(counter_play))
            break
    
    answer = input("Quieres jugar otra vez?\nSi=1.\nNo=Cualquier otro valor\n")
    if(answer != "1"):
        break

print("¡¡Gracias por jugar!!")