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

    On next screen select <i> Auto-generate a new certificate (recommended)</i> for <i> Device certificate <i>. It will create certificate files which the device uses for the authentication purpose. AWS IoT supports X.509 client certificates.

    In following screen select `iot-dht-policy` earlier and hit <i> Create thing</i> button.

    Download all the certificate files - <i> A certificate for this thing, A public key, A private key</i> and <i>A root CA</i> for AWS. 


