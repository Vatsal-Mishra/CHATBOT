from flask import Flask, request   # importing  required modules
from twilio.twiml.messaging_response import MessagingResponse   #using twilio as a server
import wikipedia
app = Flask(__name__)
@app.route('/bot', methods=['POST'])  # url for bot path and post method
def bot():
    incoming_msg = request.values.get('Body', '').lower()  # reading the question of user
    resp = MessagingResponse()   # making object of MessagingResponse
    msg = resp.message()
    responded = False
    if 'hey' in incoming_msg:               # giving different conditions for the bot
        quote = 'ALPHA at your service Sir,\nAsk me anything?'
        msg.body(quote)        # welcome msg of the bot
        responded = True
    elif 'thank' in incoming_msg:
        f='It was a pleasure helping you sir!!' # ending the conservation
        msg.body(f)
        responded =True
    else:
        g=wikipedia.summary(incoming_msg,sentences=5)    # fetching the data from wikipedia and returning first five lines.
        msg.body(g)
        responded=True
    return str(resp)   # returning the response of valid condition 
if __name__ == '__main__':
    app.run()
