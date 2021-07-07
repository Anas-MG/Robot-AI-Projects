import cv2
import threading
import time
import face_recognition
import logging
import numpy as np

logger = logging.getLogger(__name__)

thread = None

# Load a sample picture and learn how to recognize it.
anas_image = face_recognition.load_image_file("images/anas.PNG")
anas_face_encoding = face_recognition.face_encodings(anas_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    anas_face_encoding,
]
known_face_names = [
    "Anas MG !!",
]

# Initialize some variables
face_locations = []
face_encodings = []

face_names = []



class Camera:
	def __init__(self,fps=50,video_source=0):
		logger.info(f"Initializing camera class with {fps} fps and video_source={video_source}")
		self.fps = fps
		self.video_source = video_source
		self.camera = cv2.VideoCapture(self.video_source)
		
		# We want a max of 5s history to be stored, thats 5s*fps
		self.max_frames = 5*self.fps
		self.frames = []
		self.isrunning = False
		
	def run(self):
		logging.debug("Perparing thread")
		global thread
		if thread is None:
			logging.debug("Creating thread")
			thread = threading.Thread(target=self._capture_loop,daemon=True)
			logger.debug("Starting thread")
			self.isrunning = True
			thread.start()
			logger.info("Thread started")

	def _capture_loop(self):
		dt = 1/self.fps
		process_this_frame = True
		logger.debug("Observation started")
		while self.isrunning:
			
			self.stream=True
			v,im = self.camera.read()
			if v:
				
				if len(self.frames)==self.max_frames:
						self.frames = self.frames[1:]
				self.frames.append(im)

				# Resize frame of video to 1/4 size for faster face recognition processing
				small_frame = cv2.resize(im, (0, 0), fx=0.25, fy=0.25)
				# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
				rgb_small_frame = small_frame[:, :, ::-1]
				# Only process every other frame of video to save time
				if process_this_frame:
					# Find all the faces and face encodings in the current frame of video
					face_locations = face_recognition.face_locations(rgb_small_frame)
					face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
					face_names = []
					for face_encoding in face_encodings:
						# See if the face is a match for the known face(s)
						matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
						name = "Unknown"
						# # If a match was found in known_face_encodings, just use the first one.
						# if True in matches:
						#     first_match_index = matches.index(True)
						#     name = known_face_names[first_match_index]
						
						# Or instead, use the known face with the smallest distance to the new face
						face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
						best_match_index = np.argmin(face_distances)
						if matches[best_match_index]:
							name = known_face_names[best_match_index]

						face_names.append(name)
				
				# Display the results
				for (top, right, bottom, left), name in zip(face_locations, face_names):
					# Scale back up face locations since the frame we detected in was scaled to 1/4 size
					top *= 4
					right *= 4
					bottom *= 4
					left *= 4
					# Draw a box around the face
					cv2.rectangle(im, (left, top), (right, bottom), (0, 0, 255), 2)
					# Draw a label with a name below the face
					cv2.rectangle(im, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
					font = cv2.FONT_HERSHEY_DUPLEX
					cv2.putText(im, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
				
		logger.info("Thread stopped successfully")

	def stop(self):
		logger.debug("Stopping thread")
		self.isrunning = False
	def get_frame(self, _bytes=True):
		if len(self.frames)>0: 		
			if _bytes:
				img = cv2.imencode('.png',self.frames[-1])[1].tobytes()
			else:
				img = self.frames[-1]
		else:
			with open("images/not_found.jpeg","rb") as f:
				img = f.read()
		return img
		