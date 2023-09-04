from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import openai
import requests

# Initialize Flask
app = Flask(__name__)

# Twilio credentials from your Twilio dashboard
account_sid = 'AC6f7257efa585631bf192081d1e3f05ba'
auth_token = '18c58d42080521ca2c9204087a7ab78c'

# Initialize Twilio client
client = Client(account_sid, auth_token)


# Route to handle incoming calls
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    # Initialize TwiML response
    response = VoiceResponse()

    # Add a simple Say verb (This is where you'll eventually integrate Tars and Eleven Labs)
    response.say("YO YO YO Hello, this is your Tars bot speaking.")

    return str(response)

# Main executable
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)


