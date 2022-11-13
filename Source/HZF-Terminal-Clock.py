from datetime import datetime
from threading import Timer
from os import system,name

def go():
    system('cls' if name == 'nt' else 'clear')
    print(datetime.now().strftime(" ----------\n"+"| %H:%M:%S |"+"\n ----------"))
    print(datetime.now().strftime("| %d.%m.%y |"+"\n ----------"))
    timego = Timer(1, go)
    timego.start()

go()