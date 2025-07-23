import numpy as np
import cv2
import mmap
import time

WIDTH, HEIGHT, CHANNELS = 640, 480, 3
FRAME_SIZE = WIDTH * HEIGHT * CHANNELS
TOTAL_SIZE = FRAME_SIZE + 1  # 1 byte per il flag

# Nome della shared memory (deve combaciare con quello usato in C++, incluso 'Local\\')
tagname = "Local\\shm_yolo_frame"

# Apri la shared memory con mmap
mm = mmap.mmap(-1, TOTAL_SIZE, tagname, access=mmap.ACCESS_WRITE)

while True:
    mm.seek(0)
    flag = mm.read_byte()

    if flag == 1:
        frame_data = mm.read(FRAME_SIZE)
        frame = np.frombuffer(frame_data, dtype=np.uint8).reshape((HEIGHT, WIDTH, CHANNELS))
        cv2.imshow("YOLO Stream", frame)

        # Reset flag a 0
        mm.seek(0)
        mm.write_byte(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.005)

mm.close()
