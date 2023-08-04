from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import random
import datetime
import json

myMQTTClient = AWSIoTMQTTClient("iot-device-dojo-01")

myMQTTClient.configureEndpoint("a17dxerfxwfxb1-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("J:\my-github-repo\AWS-IoT-v2\certs\dht-AmazonRootCA1.pem","J:\my-github-repo\AWS-IoT-v2\certs\dht-private.pem.key", "J:\my-github-repo\AWS-IoT-v2\certs\dht-certificate.pem.crt")

myMQTTClient.connect()
print("Client Connected")

#msg = "{'Data':'Reading 1'}"
#msg='b'{\n  "message": "JetaRathod"\n}''

now = datetime.datetime.now()
time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
temp = str(random.randint(25, 44))


msg ={}
msg["Time"] = time_stamp
msg["Temperature"] = temp
msg = json.dumps(msg)
topic = "aurangabad/temperature"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent")

myMQTTClient.disconnect()
print("Client Disconnected")