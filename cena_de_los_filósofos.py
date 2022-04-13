import threading
import time

total_comidas_por_filosofo = [0, 0, 0, 0, 0]

def piensa(numero: int):
    print("El filósofo " + str(numero) + " está pensando...")
    time.sleep(1.5)

def come(numero: int, tenedores: list):
    if(total_comidas_por_filosofo[numero-1] == 5):
        print("El filosófo " + str(numero) + " ya ha comido cinco veces. Por lo que no lo hace más.")
    else:
        print("El filósofo " + str(numero) + " se prepara para comer...")
        # Determinar los tenedores que le tocan
        tenedor1 = tenedores[numero-1]
        try:
            numtenedor2 = numero
            tenedor2 = tenedores[numero]
        except:
            numtenedor2 = 0
            tenedor2 = tenedores[0]
        # Tomar los tenedores
        tomar_tenedores(tenedor1, tenedor2, numero)
        print("Se tomaron los tenedores: " + str(numero-1) + " y " + str(numtenedor2))
        # Comer
        print("El filósofo " + str(numero) + " está comiendo...")
        total_comidas_por_filosofo[numero-1] += 1
        time.sleep(1.5)
        # Soltar los tenedores
        soltar_tenedores(tenedor1, tenedor2, numero)
        total = total_comidas_por_filosofo[numero-1]
        print("El filósofo " + str(numero) + " ha comido un total de: " + str(total) + " veces.")
    
def tomar_tenedores(tenedor1 : threading.Semaphore, tenedor2: threading.Semaphore, numero: int):
    try:
        tenedor1.acquire()
        tenedor2.acquire()  
        print("El filosofo " + str(numero) + " tomó los tenedores a su izquierda y derecha...")
    except:
        print("Existió un problema al momento de tomar tenedores")

def soltar_tenedores(tenedor1 : threading.Semaphore, tenedor2: threading.Semaphore, numero:int):
    try:
        print("El filósofo " + str(numero) + " terminó de comer. Ahora suelta los tenedores...")
        tenedor1.release()
        tenedor2.release()
    except:
        print("Existió un problema al momento de soltar tenedores")

def filosofo(numero:int, tenedores:list):
    while(total_comidas_por_filosofo[numero-1] < 5):
        piensa(numero)
        come(numero, tenedores)
    print("El filosófo " + str(numero) + " ya ha comido cinco veces. Por lo que no lo hace más.")

def main():
    tenedor1 = threading.Semaphore()
    tenedor2 = threading.Semaphore()
    tenedor3 = threading.Semaphore()
    tenedor4 = threading.Semaphore()
    tenedor5 = threading.Semaphore()
    tenedores = [tenedor1, tenedor2, tenedor3, tenedor4, tenedor5]
    philosopher_list = list()
    i = 1
    while i <= 5:
        philosopher = threading.Thread(target=filosofo, args=(i,tenedores))
        philosopher_list.append(philosopher)
        time.sleep(1.5)
        i += 1
    for i in range(5):
        philosopher_list[i].start()
        
if __name__ == "__main__":
    main()
