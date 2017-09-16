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
        return self.cleanse_text(texts[0].description)

    @classmethod
    def cleanse_text(cls, text):
        text = text.encode('ascii', 'ignore')
        cleansed = []

        for word in text.split():
            if word == "duts":
                word = "puts"

            cleansed.append(word)

        return " ".join(cleansed)
