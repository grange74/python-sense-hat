from sense_hat import SenseHat
import requests

sense = SenseHat()
counter = 1

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    data = { 'id' : counter, 'temp' : t, 'humidity' : h, 'pressure' : p}
    r = requests.post("http://192.168.6.23:8080/serviceui/api/iot/sensor/data", json = data)
    print(r.status_code)
    msg = "Temp = %s, Pressure=%s, Humidity=%s" % (t,p,h)

    sense.show_message(msg)
    counter += 1