# using flask_restful 
from flask import Flask, request
from flask import Response
from flask_restplus import Api, Resource, fields
from object_detection import ObjectDetectoer
import json

import tensorflow_hub as hub
 
module_handle = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"  #

#["https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1", "https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1"]

detector = hub.load(module_handle).signatures['default']

  
app = Flask(__name__) 
 
api = Api(app) 

model = api.model('B2U_API_1',
                  {'querry': fields.String(required=True),
                   'url': fields.Url(required=False, absolute=True),
                   })

name_space = api.namespace('blind2unblind')

od = ObjectDetectoer(detector)

@name_space.route('/')
class InformationProcessing(Resource): 

    # Corresponds to POST request 
    @api.expect(model, validate=True)
    def post(self): 
          
        data = request.json

        querry = data['querry']

        url = data['url']

        objects = od.detect_objects(url)

        return Response( json.dumps(objects) , mimetype='application/json')
 

  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 