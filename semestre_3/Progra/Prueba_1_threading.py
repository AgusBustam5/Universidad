import threading
import time

def trabajador_rapido():
    thread_actual = threading.current_thread()
    print(f"{thread_actual.name} partinedo")

    time.sleep(2)
    print(f"{thread_actual.name} terminando")

def trabajador_lento():
    thread_actual = threading.current_thread()
    print(f"{thread_actual.name} partiendo")

    time.sleep(6)
    print(f"{thread_actual.name} terminando")

hilo_lento = threading.Thread(name="Hilo lento (6s)", target=trabajador_lento)
hilo_rapido_1 = threading.Thread(name="Hilo rápido (2s)", target=trabajador_rapido)
hilo_rapido_2 = threading.Thread(target=trabajador_rapido)
print("Thread principal: Fueron creados 3 threads")

print("Thread principal: Empezaré a iniciar los 3 threads")
hilo_rapido_1.start()  # Dormirá por 2 segundos
hilo_rapido_2.start()  # Dormirá por 2 segundos
hilo_lento.start()  # Dormirá por 6 segundos
print("Thread principal: Fueron iniciados 3 threads")

print()
for i in range(10):
    print(f"Thread principal: Segundo actual: {i}")
    time.sleep(1)