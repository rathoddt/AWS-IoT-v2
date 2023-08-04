# AWS-IoT-v2

IoT solution using AWS IoT Core and related services

1) Search for AWS IoT core after logging in AWS console

2) You will first create an IoT policy which authorizes the device to perform actions within AWS IoT core. Goto the IoT Core Console, click on the <b>Policies</b> option under <b>Security</b> menu in the left and then click on the <b>Create</b> a policy button.

Enter policy name : `iot-dht-policy` and paste content of `iot-policy-generic.json` then click <b>create</b>.


 3) Create a device as thing and attach the policy to it.  
 In <i>Manage</i> section click <i>All devices -> Things <ii>
