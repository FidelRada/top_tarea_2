from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)
account_sid = "AC40c157d2b7df3710b56bc6af077e7d8d"
auth_token = "a0f34e371a6903b07278fa72abb6de37"
client = Client(account_sid, auth_token)

@app.route("/", methods=["GET"])
def main():
    return "como es posible que no funcione!!"
    
@app.route("/webhook", methods=["POST"])
def receive_message():
    print(request.json)
    message_body = request.json["Body"]
    from_number = request.json["From"]
    print(message_body, from_number)
        
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='tu mensaje fue '+message_body,
        to='whatsapp:+'+from_number
    )
    
    print(message)

    return "Mensaje recibido", 200

if __name__ == "__main__":
    app.run(debug=True)