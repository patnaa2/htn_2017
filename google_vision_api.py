import io
from google.cloud import vision

vision_client = vision.Client()

with io.open('helloworld3.jpg', 'rb') as image_file:
    content = image_file.read()

image = vision_client.image(content=content)

texts = image.detect_text()
print('Texts:')

print(texts[0].description)