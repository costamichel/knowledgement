import keyboard, time, sys
from threading import Thread

a = {"value": 0}

def monitorKey():
    while True:
        if keyboard.is_pressed('q'):
            print('Você pressionou a tecla')
            a['value'] += 1 
            break                       


Thread(target = monitorKey).start()

b = [1,2,3,4,5,6,7,8]

while a['value'] == 0:
    print('>>> Olá Mundo')
    for n in b:        
        #Condição de parada
        if(a['value'] != 0):
            break
        print(n)
        time.sleep(1)

    time.sleep(1)       

print('Saiu')