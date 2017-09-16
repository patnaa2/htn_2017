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

        LOWER_ALL = False
        if all([w.isupper() for w in text.split()]):
            LOWER_ALL = True

        cleansed = []

        expecting_quotes = False

        for word in text.split():
            if word == "duts":
                word = "puts"
                expecting_quotes = True

            if expecting_quotes and '"' not in word:
                cleansed.append('"')

            if LOWER_ALL:
                word = word.lower()

            cleansed.append(word)

        return " ".join(cleansed)

if __name__ == "__main__":
    gvc = GoogleVisionClient()
    x = gvc.get_text('static/image/ruby-helloworld.jpg')
    print x
    import pdb ; pdb.set_trace()
