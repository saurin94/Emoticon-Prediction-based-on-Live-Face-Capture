import io

import time
from google.cloud.vision import types
from google.cloud import vision
import cv2
from PIL import Image

class OCR(object):

    def capture_image(self):
        path = ""
        camera = cv2.VideoCapture(0)
        i = 0
        raw_input('Press Enter to capture')
        while i < 2:
            return_value, image = camera.read()
            cv2.imwrite('opencv' + str(i) + '.png', image)
            path = "/Users/saurin/Drive/fall-17/HackHarvard/GoogleVisionCloud/" + 'opencv0.png'
            im = Image.open(path)
            im.show()
            i += 1
            break
        del (camera)
        return path


    def detect_text(self,path):
        """Detects text in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')
        t = "<p>"
        for text in texts:
            # print('\n"{}"'.format(text.description))

            t += str("{}".format(text.description)) + "<br>"
            # vertices = (['({},{})'.format(vertex.x, vertex.y)
            #             for vertex in text.bounding_poly.vertices])

            # print('bounds: {}'.format(','.join(vertices)))
        t += " </p>"
        return t
