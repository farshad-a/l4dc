import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
import time


# def on_message_print(client, userdata, message):
#     print("%s %s" % (message.topic, message.payload))
#     publish.single("/festo/actuation", message.payload)


# subscribe.callback(on_message_print, "/festo/actuation/new",
#                    hostname="127.0.0.1")

if __name__ == "__main__":
    while True:
        publish.single("/festo/actuation/new")
        time.sleep(30)
