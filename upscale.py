import cv2
from cv2 import dnn_superres
import os

IMAGES_FOLDER = 'static/images'
RESULTS_FOLDER = 'static/results'
class Upscale:
    def __init__(self, path, model, scale, image):
        # Load model
        self.path = path
        self.upscale = dnn_superres.DnnSuperResImpl_create()
        self.upscale.readModel(path)
        self.upscale.setModel(model, scale)
        
        # Load image
        self.image = image

    def upscale_image(self):
        img = cv2.imread(os.path.join(IMAGES_FOLDER, self.image))
        
        result = self.upscale.upsample(img)
        
        result_path = os.path.join(RESULTS_FOLDER, 'upscaled_' + self.image)
        
        cv2.imwrite(result_path, result)
        
        return result_path