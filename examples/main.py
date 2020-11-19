#Joypad v1.0p test code

from machine import Pin
from pyb import CAN, ADC, Timer
import utime

utime.sleep_ms(500)
print("starting Joypad v1.0p test code")
print("v1.0")
print("initializing")
can = CAN(1, CAN.LOOPBACK)
can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))


#Setup Pins
hbt_led = Pin("D13", Pin.OUT)
func_butt = Pin("D5", Pin.IN, Pin.PULL_UP)
can_wakeup = Pin("D6", Pin.OUT)
can_wakeup.value(0) 

X_POT = ADC("A0")
Y_POT = ADC("A1")

START_BUTTON = Pin("E5", Pin.IN, Pin.PULL_UP)
SELECT_BUTTON = Pin("E6", Pin.IN, Pin.PULL_UP)
GREEN_BUTTON = Pin("E15", Pin.IN, Pin.PULL_UP)
YELLOW_BUTTON = Pin("E8", Pin.IN, Pin.PULL_UP)
RED_BUTTON = Pin("E13", Pin.IN, Pin.PULL_UP)
BLUE_BUTTON = Pin("E11", Pin.IN, Pin.PULL_UP)

UP_BUTTON = Pin("E1", Pin.IN, Pin.PULL_UP)
DOWN_BUTTON = Pin("D1", Pin.IN, Pin.PULL_UP)
LEFT_BUTTON = Pin("E3", Pin.IN, Pin.PULL_UP)
RIGHT_BUTTON = Pin("E2", Pin.IN, Pin.PULL_UP)
PUSH_BUTTON = Pin("D0", Pin.IN, Pin.PULL_UP)

JOY_BUTTON = Pin("E0", Pin.IN, Pin.PULL_UP)

BUZZER_PIN = Pin('A2')

BUZZER_FREQ = Timer(3, freq = 240)
buzzer = BUZZER_FREQ.channel(1, Timer.PWM, pin=BUZZER_PIN)
buzzer.pulse_width_percent(0)
BUZZER_FREQ.deinit()

#Setup leds
BLUE_LED = Pin("E10", Pin.OUT)
RED_LED = Pin("E12", Pin.OUT)
YELLOW_LED = Pin("SD_DETECT", Pin.OUT)
GREEN_LED = Pin("E14", Pin.OUT)
    
#Setup hbt timer
hbt_state = 0
hbt_interval = 500
start = utime.ticks_ms()
next_hbt = utime.ticks_add(start, hbt_interval)
hbt_led.value(hbt_state)


print("starting")


def chk_hbt():
    global next_hbt
    global hbt_state
    now = utime.ticks_ms()
    if utime.ticks_diff(next_hbt, now) <= 0:
        if hbt_state == 1:
            hbt_state = 0
            hbt_led.value(hbt_state)
            #print("hbt")
        else:
            hbt_state = 1
            hbt_led.value(hbt_state)  
        
        next_hbt = utime.ticks_add(next_hbt, hbt_interval)

def chk_buttons():
    global next_button_chk
    now = utime_ms()
    if utime.ticks_diff(next_button_chk, now) <= 0:
        pass
        

def send():
    can.send('EVZRTST', 123)   # send a message with id 123
    
def get():
    mess = can.recv(0)
    print(mess)
    do_animation()
    do_animation()
    do_animation()
    do_animation()

def do_animation():
    BLUE_LED.value(1)
    utime.sleep_ms(100)
    BLUE_LED.value(0)
    utime.sleep_ms(100)
    RED_LED.value(1)
    utime.sleep_ms(100)
    RED_LED.value(0)
    utime.sleep_ms(100)
    YELLOW_LED.value(1)
    utime.sleep_ms(100)
    YELLOW_LED.value(0)
    utime.sleep_ms(100)
    GREEN_LED.value(1)
    utime.sleep_ms(100)
    GREEN_LED.value(0)
    utime.sleep_ms(100)

while True:
    chk_hbt()
    if not (func_butt.value()):
        print("function button")
        send()
        utime.sleep_ms(200)
    
    if can.any(0):
        get()

    if not (START_BUTTON.value()):
        print("START_BUTTON button:", X_POT.read(), Y_POT.read())
        utime.sleep_ms(200)

    if not (SELECT_BUTTON.value()):
        print("SELECT_BUTTON button")
        BUZZER_FREQ = Timer(3, freq = 52)
        buzzer = BUZZER_FREQ.channel(1, Timer.PWM, pin=BUZZER_PIN)
        buzzer.pulse_width_percent(30)
        utime.sleep_ms(100)
        BUZZER_FREQ.freq(200)
        utime.sleep_ms(100)
        BUZZER_FREQ.freq(400)
        utime.sleep_ms(100)
        BUZZER_FREQ.freq(800)
        utime.sleep_ms(100)
        BUZZER_FREQ.freq(1000)
        utime.sleep_ms(100)
        BUZZER_FREQ.freq(1200)
        utime.sleep_ms(100)
        BUZZER_FREQ.freq(1500)
        BUZZER_FREQ.deinit()
        
    if not (GREEN_BUTTON.value()):
        print("GREEN_BUTTON button")
        utime.sleep_ms(200)
        
    if not (RED_BUTTON.value()):
        print("RED_BUTTON button")
        utime.sleep_ms(200)
        
    if not (YELLOW_BUTTON.value()):
        print("YELLOW_BUTTON button")
        utime.sleep_ms(200)
        
    if not (BLUE_BUTTON.value()):
        print("BLUE_BUTTON button")
        utime.sleep_ms(200)
        
    if not (UP_BUTTON.value()):
        print("UP_BUTTON button")
        utime.sleep_ms(200)
            
    if not (DOWN_BUTTON.value()):
        print("DOWN_BUTTON button")
        utime.sleep_ms(200)

    if not (LEFT_BUTTON.value()):
        print("LEFT_BUTTON button")
        utime.sleep_ms(200)

    if not (RIGHT_BUTTON.value()):
        print("RIGHT_BUTTON button")
        utime.sleep_ms(200)
        
    if not (PUSH_BUTTON.value()):
        print("PUSH_BUTTON button")
        utime.sleep_ms(200)

    if not (JOY_BUTTON.value()):
        print("JOY_BUTTON button")
        utime.sleep_ms(200)



        