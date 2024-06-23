import cv2

config_model = 'mobilenet_and_coco.txt'
frozen_model = 'frozen model.pb'

model = cv2.dnn_DetectionModel(config_model,frozen_model)


class_labels = []
file_name = 'labels.txt'
with open(file_name, 'rt') as fpt:
  class_labels = fpt.read().rstrip('\n').split('\n')

model.setInputSize(200,200)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

# UPLOADING FOR AN VIDEO FILE

cap = cv2.VideoCapture('Streets.mp4')

if not cap.isOpened():
  cap = cv2.VideoCapture(0)
if not cap.isOpened():
  raise IOError("Cant Open the video")


font_scale=3
font = cv2.FONT_HERSHEY_PLAIN

while True:
  ret,frame = cap.read()
  # Inside the while loop, before displaying the frame
  cv2.namedWindow('Object Detection Program', cv2.WINDOW_NORMAL)  # Create a resizable window
  cv2.resizeWindow('Object Detection Program', frame.shape[1],
                   frame.shape[0])  # Resize the window to match the frame size
  cv2.imshow('Object Detection Program', frame)
  ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.55)
  print(ClassIndex)
  if(len(ClassIndex) != 0):
    for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
      if (ClassInd <=80):
        cv2.rectangle(frame, boxes, (0, 0, 255), 4)
        cv2.putText(frame,class_labels[ClassInd-1],(boxes[0]+10, boxes[1]+40), font, fontScale=font_scale, color=(0,255,0), thickness=3)
  cv2.imshow('Object Detection Program', frame)
  if cv2.waitKey(2) & 0xff == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()