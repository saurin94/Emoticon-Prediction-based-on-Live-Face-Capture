import io
import emoji
from google.cloud.vision import types
from google.cloud import vision
import cv2
from PIL import Image



def capture_image():
    path = ""
    camera = cv2.VideoCapture(0)
    i = 0
    while i < 10:
        raw_input('Press Enter to capture')
        return_value, image = camera.read()
        cv2.imwrite('opencv' + str(i) + '.png', image)
        path = "/Users/saurin/Drive/fall-17/HackHarvard/GoogleVisionCloud/" + 'opencv0.png'
        im = Image.open(path)
        im.show()
        i += 1
        break
    del (camera)
    return path


def detect_faces(path):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations
    # print faces
    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    # print('Faces:')

    for face in faces:
        d = {}
        d['anger'] = '{}'.format(likelihood_name[face.anger_likelihood])
        d['joy'] = '{}'.format(likelihood_name[face.joy_likelihood])
        d['surprise'] = '{}'.format(likelihood_name[face.surprise_likelihood])
        d['sorrow'] = '{}'.format(likelihood_name[face.sorrow_likelihood])
        # print d

        for emotion, probab in d.iteritems():
            if probab == 'VERY_LIKELY' or probab == 'POSSIBLE':
                print "suggest " + emotion + " smileys !!!!"
                # print('face bounds: {}'.format(','.join(vertices)))

    landmarks_response = client.landmark_detection(image=image)
    landmark = landmarks_response.landmark_annotations
    for l in landmark:
        print "Landmark :", l

    responses = client.label_detection(image=image)
    labelss = responses.label_annotations
    print('Labels:')

    #predictive_smileys = []
    for label in labelss:
        try:
            if label.description == "hand":
                label.description = "+1"
            val = emoji.emojize(':' + str(label.description) + ':', use_aliases=True)
            if val != ':' + str(label.description) + ':':
                print val
        except Exception, e:
            print "Label not mapped to smiley :", label.description

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

path = capture_image()
# path = "/Users/saurin/Drive/fall-17/HackHarvard/GoogleVisionCloud/image1.jpg"
detect_faces(path)
detect_text(path)