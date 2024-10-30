import cv2
from cv2 import dnn_superres

sr = dnn_superres.DnnSuperResImpl_create()	

# path = "LapSRN_x8.pb"
path = 'models/EDSR_x4.pb'
# path = "4x-UltraSharp.pth"
# path = "edsr_x4-4f62e9ef.pth"

sr.readModel(path)

# sr.setModel('edsr', 4)
# sr.setModel('lapsrn', 8)
sr.setModel('edsr', 4)

# sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CPU)
# sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

img = cv2.imread('static/images/comic.png')

result = sr.upsample(img)

cv2.imwrite('static/images/comic.png', result)