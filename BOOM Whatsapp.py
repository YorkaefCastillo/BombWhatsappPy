import pyautogui, webbrowser
import time

Ador, Titulo = "","bombarde a whatsapp"
#Adornat Titulo
print(f"{Ador.center(50,'*')}")
print(f"{Titulo.center(50).upper()}")
print(f"{Ador.center(50,'*')}")

indicador = int(input("Ingrese su indicador de pais: ")) #<- Indicador de pais es 501,502,54 etc
victima = int(input("Ingrese numero de la victima: "))
mensaje = str(input("Mensaje: "))
Cantidad = int(input("\nCuentos Mensajes quiere enviar: "))

#Envio de mensajes 
def Envio():
    webbrowser.open(f"https://web.whatsapp.com/send?phone=+{indicador}{victima}")
    time.sleep(30) #Tiempo de espera para que carge el navegador y entre a whatsapp web 
 
 #Bucle para enviar varios mensajes
    for i in range(Cantidad):
        pyautogui.typewrite(f"{mensaje}")
        pyautogui.press('enter')
        
    print("Mensajes envidos con exito")



Envio()