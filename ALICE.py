from flask import Flask, request, send_file
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from openai import OpenAIAPI
from elevenlabs import set_api_key
import requests

# Initialize Flask
app = Flask(__name__)

# Twilio credentials from your Twilio dashboard
account_sid = 'AC6f7257efa585631bf192081d1e3f05ba'
auth_token = '18c58d42080521ca2c9204087a7ab78c'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Initialize OpenAI
openai_api = OpenAIAPI(api_key="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")

# Initialize Eleven Labs
set_api_key("74821b28102ee9a88cd2a98cbef6da54")

# Generate text response using OpenAI GPT
def generate_response(prompt):
    model_engine = "gpt-4-32k-0314"  # Or any other model
    response = openai_api.create_completion(model=model_engine, prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

# Generate audio using Eleven Labs
def generate_audio(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/ALICE/stream"
    headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": "74821b28102ee9a88cd2a98cbef6da54"
    }
    data = {
      "text": text,
      "model_id": "eleven_monolingual_v1"
    }
    response = requests.post(url, json=data, headers=headers, stream=True)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return 'output.mp3'

# Route to handle incoming calls
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    # Initialize TwiML response
    response = VoiceResponse()
    
    # Generate response and audio
    prompt = "Hello, how can I assist you today?"
    text = generate_response(prompt)
    audio_file = generate_audio(text)
    
    # Add generated audio to TwiML response (You'll need to host this file somewhere accessible by Twilio)
    response.play('URL_TO_YOUR_HOSTED_output.mp3')

    return str(response)

# Main executable
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)



