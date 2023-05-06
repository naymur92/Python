"""
Prerequisite for this programme
1. install CMake on machine
2. install dlib
3. install PIL library for python
4. install face_recognition library for python
"""

# Find faces in picture
# https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py

from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("20230227_180209.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
  # Print the location of each face in this image
  top, right, bottom, left = face_location

  # You can access the actual face itself like this:
  face_image = image[top:bottom, left:right]
  pil_image = Image.fromarray(face_image)
  pil_image.show()
