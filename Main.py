from flask import Flask, jsonify
from Config import key
import openai
from openai import OpenAI
from flask import render_template

client = OpenAI()
openai.api_key = key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('Index.html', )

@app.route('/generateimages/<prompt>')
def generate(prompt):
    print("prompt:", prompt)
    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="256x256",
      quality="standard",
      n=5,
    )
    print(response)
    image_url = response.data[0].url
    return jsonify(response)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)