import tensorflow as tf
import tensorflow_hub as hub
 
import cv2
from urllib.request import urlopen
import numpy as np


class  ObjectDetectoer(object):

	"""docstring for  ObjectDetectoer"""
	def __init__(self, detector ):
		super( ObjectDetectoer, self).__init__()
		self.detector = detector 

	

	def get_image(self, url):

	    with urlopen(str(url.numpy().decode("utf-8"))) as request:
	        img_array = np.asarray(bytearray(request.read()), dtype=np.uint8)

	    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
	    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



	def read_image_from_url(self, url):

	    return tf.py_function(self.get_image, [url], tf.uint8)



	def run_detector(self, detector, img):

	  converted_img  = tf.image.convert_image_dtype(img, tf.float32)[tf.newaxis, ...]
	  result = detector(converted_img)
	  result = {key:value.numpy() for key,value in result.items()}

	  #print("Found %d objects." % len(result["detection_scores"]))

	  return result


	def detect_objects(self, url, min_score=0.1):

	  det = self.detector
	  img = self.read_image_from_url(url)
	  det_opt = self.run_detector(det, img)

	  ret = list()
	  
	  for obj,score in zip(det_opt["detection_class_entities"],det_opt["detection_scores"]):
	    if score > min_score :
	      ret.append((str(obj),str(score)))

	  return dict(ret)

