import os
from Config import key
import openai
from openai import OpenAI

client = OpenAI()
openai.api_key = key

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)