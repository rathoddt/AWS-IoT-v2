# AWS-IoT-v2

IoT solution using AWS IoT Core and related services

1) Search for AWS IoT core after logging in AWS console

2) You will first create an IoT policy which authorizes the device to perform actions within AWS IoT core. Goto the IoT Core Console, click on the <i>Policies</i> option under <i>Security</i> menu in the left and then click on the <i>Create</i> a policy button.

    Enter policy name : `iot-dht-policy` and paste content of `iot-policy-generic.json` then click <i>create</i>.


 3) Create a device as thing and attach the policy to it.  
 In <i>Manage</i> section click <i>All devices -> Things <ii>

    In a window that opens click <i> Create things</i>  
    --> Create single thing</i>
    Enter thing name- <i>City-temperature </i>

    On next screen select <i> Auto-generate a new certificate (recommended)</i> for <i> Device certificate </i>. It will create certificate files which the device uses for the authentication purpose. AWS IoT supports X.509 client certificates.

    In following screen select `iot-dht-policy` earlier and hit <i> Create thing</i> button.

    Download all the certificate files - <i> A certificate for this thing, A public key, A private key</i> and <i>A root CA</i> for AWS. 

4) Go to <i> Test  -> MQTT Test Client </i> copy endpoint and paste into `Publish-Device-to-AWS-IoT-Core.py` as below:
    ```
    #Note endpoint with yours
    myMQTTClient.configureEndpoint("a17dxerfxwfxb1-ats.iot.us-east-1.amazonaws.com", 8883)
    ```

    Since there is no physical device for,  Python code will simulates as the device (termperature sensor) communicating with the AWS IoT Core.

5) Click <i> Subcribe to topic </i> in <i> Topic filter </i> enter topic name e.g. `aurangabad/temperature` and hit <i> Subscribe</i>

6) Configure certificate and key paths for device suthenticationa and secure communication in `Publish-Device-to-AWS-IoT-Core.py`
    ```
    myMQTTClient.configureCredentials("dht-AmazonRootCA1.pem","dht-private.pem.key", "dht-certificate.pem.crt")
    ```

7) Run `Publish-Device-to-AWS-IoT-Core.py` program
    ```
    python Publish-Device-to-AWS-IoT-Core.py
    ```

    If everthing is configured properly you should see the temperature value in json format in AWS Console

    This program can be modified to runn in loop and send data at regular interval.


