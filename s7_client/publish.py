import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
import time
openBrac = "{"
closeBrac = "}"


def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    publish.single("/festo/actuation", message.payload)


subscribe.callback(on_message_print, "/festo/actuation/new",
                   hostname="127.0.0.1")

if __name__ == "__main__":
    while True:
        for i in range(4):
            for j in range(5):
                for k in range(6):
                    publish.single(
                        "/festo/actuation", f'{openBrac}"vacuum": {i}, "screw": {j}, "vibration":{k}{closeBrac}')
    time.sleep(30)
