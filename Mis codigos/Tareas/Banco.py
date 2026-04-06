saldo = 50000

print("Hola, bienvenido a Banco Estado")

opcion_escogida = int(input("¿Que operaciòn necesita realizar?\n(1)Ver saldo\n(2)Girar dinero\n(3)Inversiòn\n(4)Salir\n"))
while True:
    if opcion_escogida == 1:
        
        print(f"Su saldo es de {saldo}")
        
        otra_operacion = input("¿Necesita realiar la misma operaciòn?").lower
        
        if otra_operacion == "no":
            print("Cajero cerrado")
        elif otra_operacion == "si":
            print()
            

    elif opcion_escogida == 2:
        
        retiro = int(input("¿Cuanto dinero desea retirar?"))
        
        if retiro > saldo:
            print(f"Error. Recuerde que su saldo es de {saldo}")
        elif retiro <= saldo:
            saldo = saldo - retiro
            print(f"Dinero retirado {retiro}. Ahora su saldo es de {saldo}")
            otra_operacion = input("¿Desea realizar la misma operaciòn?").lower
            if otra_operacion == "no":
                print("Gracias por elegir Banco Estado")
                exit()
            elif otra_operacion == "si":
                print()
            else:
                print("Opcion invalida")

    elif opcion_escogida == 3:
        inversion = int(input("¿cuanto desea invertir?"))
        if inversion <= saldo:
            inversion = inversion * 2
            saldo = inversion + saldo
            print(f"Felicidades. Su sueldo actual es de {saldo}")
        elif inversion > saldo:
            inversion = input(f"Excede de tu presupuesto. Intente con una cantidad menor, recuerde que su saldo es de {saldo}")
        print(f"Felicidades. Su sueldo actual es de {saldo}")
        otra_operacion = input("¿Desea realizar la misma operaciòn?").lower
        if otra_operacion == "no":
            print("Gracias por elegir Banco Estado")
            exit()
        elif otra_operacion == "si":
            print()

    elif opcion_escogida == 4:
        print("Cajero apagado")
        exit()
    else:
        print("Opciòn invàlida")



            
    

    

