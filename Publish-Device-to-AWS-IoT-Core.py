from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
#import sys
import random
import datetime
import json

myMQTTClient = AWSIoTMQTTClient("city_temp")

myMQTTClient.configureEndpoint("a2pd5j14ci20op-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("J:\my-github-repo\AWS-IoT-v2\certs\sensor02-AmazonRootCA1.pem","J:\my-github-repo\AWS-IoT-v2\certs\sensor02-private.pem.key", "J:\my-github-repo\AWS-IoT-v2\certs\sensor02-certificate.pem.crt")

myMQTTClient.connect()
print("Client Connected")

#msg = "{'Data':'Reading 1'}"
#msg='b'{\n  "message": "JetaRathod"\n}''

now = datetime.datetime.now()
time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
temperature = str(random.randint(25, 44))


msg ={}
msg["Time"] = time_stamp
msg["Temperature"] = temperature
msg = json.dumps(msg)
print("Message:", msg)
topic = "aurangabad/temperature"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent")

myMQTTClient.disconnect()
print("Client Disconnected")