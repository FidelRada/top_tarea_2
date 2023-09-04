
import os
from twilio.rest import Client

#para mandar mensajes

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = "AC40c157d2b7df3710b56bc6af077e7d8d"
auth_token = "a0f34e371a6903b07278fa72abb6de37"
client = Client(account_sid, auth_token)

message = client.messages.list(
  #from_='whatsapp:+14155238886',
  #body='YOLOSAN',
  to='whatsapp:+59160910990'
)

print(message)

for m in message:
    print(m.to, m.body)