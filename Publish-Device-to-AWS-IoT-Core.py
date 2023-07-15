from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys

myMQTTClient = AWSIoTMQTTClient("iot-device-dojo-01")

myMQTTClient.configureEndpoint("a2wl4jltyrahn6-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("J:\my-github-repo\AWS-IoT-v2\certs\AmazonRootCA1.pem","J:\my-github-repo\AWS-IoT-v2\certs\private.pem.key", "J:\my-github-repo\AWS-IoT-v2\certs\certificate.pem.crt")

myMQTTClient.connect()
print("Client Connected")

#msg = "{'Data':'Reading 1'}"
msg='{"message": "Reading 5"}'
topic = "general/inbound"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent")

myMQTTClient.disconnect()
print("Client Disconnected")