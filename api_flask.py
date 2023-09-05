import os
from api_chatGPT import ChatGPT
from flask import Flask, request
#from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
account_sid = os.environ['sid'] #"AC40c157d2b7df3710b56bc6af077e7d8d"
auth_token = os.environ['token'] #"734a6fa7afd32245c4b5ed4cbc3313fd"
#client = Client(account_sid, auth_token)
gpt = ChatGPT(os.environ['key_gpt'])

@app.route("/", methods=["GET"])
def main():
    return "como es posible que no funcione!!"
    
@app.route("/webhook", methods=["POST", "GET"])
def receive_message():

    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    body = request.values.get('Body', None)
    # Add a message
    #resp.message("The Robots are coming! Head for the hills!")
    try:
        respGPT = gpt.get_response(body)
    except :
        print("paso algo con el GPT")
    
    try:
        resp.message(respGPT)#(body)#("hola como estas")
    except:
        print("paso algo con el twilio")

    return str(resp)

    """try:
        print(request.json)
        message_body = request.json["Body"]
        from_number = request.json["From"]
        print(message_body, from_number)
        
        print("ocuario algo en el json")
        
        
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='tu mensaje fue '+message_body,
            to='whatsapp:+'+ from_number #59160910990'
        )
        
        print(message)
        return "Mensaje recibido", 200
    except:
        print("ocurrio algo")
        return "ocurrio algo", 400
        """

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)
    