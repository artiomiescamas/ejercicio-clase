#esto es un programa en el que el ordenador elija 
# un número al azar entre 1 y 10, y le pida al usuario
#  que intente adivinarlo. Si el usuario adivina correctamente,
#  el programa debe mostrar "
# ¡Correcto!".Si no, debe mostrar "Sigue intentando"
NUM_ALEATORIO = 3
print("dime un numero del 1 al 10")
numero= int(input())
if(numero==NUM_ALEATORIO):
    print("has acertado")
else:
    print("sigus intentando")
    