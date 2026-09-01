from wifi import connect_wifi
from machine import Pin, PWM

sound = PWM(Pin(14))
sound.freq(2700)
sound.duty_u16(0)

status_led = Pin(15,1)

print(connect_wifi())

if connect_wifi():
    status_led.value(1)
    sound.duty_u16(100)