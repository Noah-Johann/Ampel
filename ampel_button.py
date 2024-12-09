from gpiozero import LED, Button
from time import sleep

ROT = LED()
GELB = LED()
GRUEN = LED()
BLAU = LED()
button = Button()

def traffic_light():

    try:
        while True:
            #Gruenphase
            ROT.off()
            BLAU.off()
            GELB.off()
            GRUEN.on()

            if button.is_pressed:
                #Gelbphase
                GRUEN.off()
                GELB.on()
                sleep(1.5)

                #Rotphase
                ROT.on()
                GELB.off()

                #Fußgängerampel
                for __ in range(14):
                    BLAU.on()
                    sleep(0.5)
                    BLAU.off()
                    sleep(0.5)
                
                GELB.on()
                sleep(2.5)


    finally:
        ROT.off()
        GELB.off()
        GRUEN.off()
        BLAU.off()
