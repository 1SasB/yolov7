import paho.mqtt.client as mqtt 

mqttBroker ="" 

client = mqtt.Client("OpenFire_Confidence")

try:
    client.connect(mqttBroker)
except Exception as e:
    print("Could not connect to Mqtt Broker")
    print(e)

def publish_confidence(confidence):
    try:
        client.publish("stat/OSFD/LR/confidence", confidence)
        print("Just published " + str(confidence) + " to topic stat/OSFD/LR/confidence")
    except Exception as e:
        print("Something Went Wrong. Couldnt Publish To stat/OSFD/LR/confidence")
        print(e)


    