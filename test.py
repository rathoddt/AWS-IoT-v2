import time
import random

t=time.strftime('%X %x %Z')

print(t)

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


print(time.strftime('%H:%M%p %Z on %b %d, %Y'))


import json

data = {}
data['key1'] = 'value1'
data['key2'] = 'value2'
json_data = json.dumps(data)

print(json_data)

now = datetime.datetime.now()
time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
temp = str(random.randint(25, 44))

msg ={}
msg["Time"] = time_stamp
msg["Temperature"] = temp
msg = json.dumps(msg)
print(msg)