import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
def customCallback(client,userdata,message):
    print("callback came...")
    print(message.payload)



myMQTTClient = AWSIoTMQTTClient("iot-device-dojo-01")

myMQTTClient.configureEndpoint("a2wl4jltyrahn6-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("J:\my-github-repo\AWS-IoT-v2\certs\AmazonRootCA1.pem","J:\my-github-repo\AWS-IoT-v2\certs\private.pem.key", "J:\my-github-repo\AWS-IoT-v2\certs\certificate.pem.crt")

myMQTTClient.connect()
print("Client Connected")

myMQTTClient.subscribe("general/outbound", 1, customCallback)
print('waiting for the callback. Click to conntinue...')
x = input()

myMQTTClient.unsubscribe("general/outbound")
print("Client unsubscribed") 


myMQTTClient.disconnect()
print("Client Disconnected")