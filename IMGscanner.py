import cv2 as cv
import numpy


MyDict = {55: 'orange'}


class Detector:
    def __init__(self):
        global cvNet
        cvNet = cv.dnn.readNetFromTensorflow('model/frozen_inference_graph.pb',
                                             'model/ssd_mobilenet_v1_coco_2017_11_17.pbtxt')

    def detectObject(self, imName):
        img = cv.cvtColor(numpy.array(imName), cv.COLOR_BGR2RGB)
        cvNet.setInput(cv.dnn.blobFromImage(img, 0.007843, (300, 300), (127.5, 127.5, 127.5), swapRB=True, crop=False))
        detections = cvNet.forward()
        cols = img.shape[1]
        rows = img.shape[0]
        counter = 0
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.4:
                class_id = int(detections[0, 0, i, 1])
                if class_id in MyDict:
                    xLeftBottom = int(detections[0, 0, i, 3] * cols)
                    yLeftBottom = int(detections[0, 0, i, 4] * rows)
                    xRightTop = int(detections[0, 0, i, 5] * cols)
                    yRightTop = int(detections[0, 0, i, 6] * rows)

                    cv.rectangle(img, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop), (0, 255, 0), 2)
                if class_id in MyDict:
                    counter += 1
                    label = MyDict[class_id] + " :"
                    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 2)
                    yLeftBottom = max(yLeftBottom, labelSize[1])
                    cv.putText(img, label, (xLeftBottom+5, yLeftBottom), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
        Count = cv.putText(img, ("{}".format(counter)), (10, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv.LINE_AA, False) 
        img = cv.imencode('.jpg', img)[1].tobytes()
        return img
