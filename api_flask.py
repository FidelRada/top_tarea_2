import os
from api_chatGPT import ChatGPT
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
gpt = ChatGPT(os.environ['key_gpt'])

@app.route("/", methods=["GET"])
def main():
    return "como es posible que no funcione!!"
    
@app.route("/webhook", methods=["POST", "GET"])
def receive_message():

    resp = MessagingResponse()

    body = request.values.get('Body', None)
    try:
        respGPT = gpt.get_response(body)
    except :
        print("paso algo con el GPT")
    
    try:
        resp.message(respGPT)
    except:
        print("paso algo con el twilio")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)
    