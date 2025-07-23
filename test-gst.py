import cv2
pipeline = "udpsrc port=5000 ! application/x-rtp, encoding-name=H264 ! rtph264depay ! avdec_h264 ! videoconvert ! appsink"
cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
print("opened:", cap.isOpened())
