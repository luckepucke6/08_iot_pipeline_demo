from wifi import connect_wifi
from machine import Pin, PWM
from dht import DHT11

sound = PWM(Pin(14))
sound.freq(2700)
sound.duty_u16(0)

status_led = Pin(15,1)
dht_sensor = DHT11(Pin(16,1))

print(connect_wifi())

if connect_wifi():
    status_led.value(1)
    sound.duty_u16(100)

while True:
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    data = {"temperature": temp, "humidity": humidity}
    print(data)