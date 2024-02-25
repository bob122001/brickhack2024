#Ai helper functions
from openai import OpenAI
client = OpenAI()

def generate_image(prompt):

    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url

def generate_variation_from_image():
    response = client.images.create_variation(
    image=open("image_edit_original.png", "rb"),
    n=2,
    size="1024x1024"
    )

    image_url = response.data[0].url