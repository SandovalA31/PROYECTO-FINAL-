print("BIEN BENIDO AL JUEGO ")
print("fecha: 22/12/2024")
print("Nombre: Sandoval Anthony")
print("Tema: Proyecto Final")

("Aplicacion del sofware: a continuacion podemos ver los sisguientes comando que yo utlice para desarrollar el video juego de piedra, papel o tojera ")
("comence con los comando true y while, dando el int y el imput para generar lo que seria la extructura del video juego ")

while True: 
    a = int(input("jugador 1: 1=piedra, 2=papel, 3=tijera: "))
    b = int(input("jugador 2: 1=piedra, 2=papel, 3=tijera: "))

    ("Con la finalidad depues genere lo que seria el desarrolo del juego codificando la generacion y la extructura de comandos ")
    ("genere lo que es lo que se puede lo que nose puede al ganador y el empate ")

    if a == 1 and b == 3:
        print('jugador 1 Gana: Piedra gana a tijera')
    elif a == 2 and b == 1: 
        print('jugador 1 Gana: Papel gana a piedra')
    elif a == 3 and b == 2: 
        print('jugador 1 Gana: tijera gana a Papel')
    elif b == 1 and a == 3: 
        print('jugador 2 Gana: piedra gana a tijera')
    elif b == 2 and a == 1: 
        print('jugador 2 Gana: Papel gana a Piedra')
    elif b == 3 and a == 2: 
        print('jugador 2 Gana: Tijera gana a Papel')
    else:
        print('ninguno gana ')
 
 
("Como finalidad despues de aver desarrolado el video juego me quede con la duda y el hambre de poder desarrolar para no solo para dos usuaios ")
("sino para 4 o 5 jugadores mas ")




