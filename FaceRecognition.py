import face_recognition
from PIL import Image, ImageDraw
import numpy as np

Obama_image = face_recognition.load_image_file("Obama.jpg")
Obama_face_encoding = face_recognition.face_encodings(Obama_image)[0]

Donald_image = face_recognition.load_image_file("Donald.jpg")
Donald_face_encoding = face_recognition.face_encodings(Donald_image)[0]

known_face_names = [
    "Obama",
    "Donald"
]

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Bill"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(48, 63, 159))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(48, 63, 159), outline=(48, 63, 159))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 0))

del draw
pil_image.show()


        # End of FaceRecognition program