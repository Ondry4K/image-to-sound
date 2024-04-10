#credit me plz – Ondry
import requests
import base64
from io import BytesIO
from PIL import Image
import numpy as np
from scipy.io.wavfile import write

def meow(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image_bytes = BytesIO(response.content)
        base64_image = base64.b64encode(image_bytes.read()).decode('utf-8')
        image = Image.open(BytesIO(base64.b64decode(base64_image)))
        image = image.convert('L')
        image_array = np.array(image)
        sorted_array = image_array.reshape(-1)
        write("image_audio.wav", 44100, sorted_array)
        print("[-] congratz you now hab audio!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_url = input("[+] Image URL: ")
    meow(image_url)
