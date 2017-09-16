import io
from google.cloud import vision

class GoogleVisionClient(object):

    def __init__(self):
        self._vision_client = vision.Client()

    def get_text(self, filename):
        with io.open(filename, 'rb') as image_file:
            content = image_file.read()

        image = self._vision_client.image(content=content)

        texts = image.detect_text()
        return texts[0].description
