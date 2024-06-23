<h1 align="center">Object Detection Model using Cv2 👨‍💻 </h1>
<br/>
<img align="right" height="270" width="430" src="https://miro.medium.com/v2/resize:fit:1200/0*e9eu2a2tZyI2qCfN.gif" />
 🔭 This project demonstrates real-time object detection using OpenCV (cv2), the MobileNet deep learning model, and the COCO dataset. It leverages a pre-trained frozen inference graph for efficient object identification within images or video streams.
<h2 align="left">Requirements </h2>
-Python 3.x
<br/>
-OpenCV (cv2) library
<br/>
-Pre-trained MobileNet, COCO model files and Frozen model (download them to local pc)
<br/>
<h2 align="left">Usage </h2>
-The program automatically attempts to open the video file Streets.mp4(You can upload your own videos). If the file is unavailable, it defaults to your webcam stream.
<br/>
-A window titled "Object Detection Program" will display the video feed with detected objects highlighted.
<br/>
-Bounding boxes will be drawn around detected objects, and their corresponding class labels will be displayed.(Note:Only Objects that are labeled in labels.txt file are displayed)
<br/>
-You can adjust the confidence threshold (confThreshold=0.55) in the code to control the minimum confidence required for a detection to be displayed.
<br/>
-Press the 'q' key to exit the program.
<h2 align="left">Explanation </h2>
<h3 align="left">Imports</h3>
-The script imports necessary modules, including OpenCV (cv2)
<h3 align="left">Model and Label Loading</h3>
-The model configuration file (mobilenet_and_coco.txt) and the frozen inference graph (frozen_model.pb) are loaded using cv2.dnn_DetectionModel.
<br/>
-Class labels are read from labels.txt and stored in a list class_labels.
<h3 align="left">Model Configuration</h3>
-The model's input size is set to 200x200 pixels.
<br/>
-The input scale and mean values are adjusted for normalization.
<br/>
-The input color channel order is swapped to BGR (OpenCV's default) if necessary.
<h3 align="left">Video Capture</h3>
-A video capture object cap is created, attempting to open the video file Streets.mp4 first. It then falls back to the webcam if the file is not found.
<br/>
-Error handling is included to raise an exception if video capture fails.
<h3 align="left">Main Loop</h3>
-The loop continuously reads frames from the video stream using cap.read().
<br/>
-The frame is resized to match the model's expected input size using OpenCV's resizing functions.
<br/>
-model.detect is used for object detection in the frame. It returns class indices, confidence scores, and bounding boxes for detected objects that meet the specified confidence threshold.
<br/>
-For each detected object:

<br/>
1)A bounding box is drawn around the object using cv2.rectangle.
<br/>
2)The corresponding class label from class_labels is retrieved and displayed on the frame using cv2.putText.
<br/>
-The processed frame is displayed in the "Object Detection Program" window.
<br/>
-The program exits when the 'q' key is pressed.
You can modify the script to:
-The video capture object is released using cap.release().
<br/>
-OpenCV windows are destroyed using cv2.destroyAllWindows().
<h2 align="left">Customization </h2>
<h3 align="left">You can modify the script to:</h3>
-Use a different video file or image set for object detection.
<br/>
-Experiment with different confidence thresholds (confThreshold) to adjust the detection sensitivity.
<br/>
-Explore ways to integrate this object detection functionality into a larger application.
<h2 align="left">Further Considerations</h2>
-The pre-trained MobileNet model may not be ideal for all object detection tasks. Consider exploring other models or fine-tuning the provided model on your specific dataset for improved accuracy.
<br/>
-The script currently processes frames one by one. For more efficient real-time performance, you might investigate techniques like multithreading or GPU acceleration.








