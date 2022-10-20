import cv2
vidcap = cv2.VideoCapture('vid.mp4')
success, image = vidcap.read()
count = 1
cnt = 1
while success:
  if count % 100 == 0
    cv2.imwrite("video_data/image_%d.jpg" % cnt, image)   
    cnt = cnt +1 
    success, image = vidcap.read()
    print('Saved image ', count)
  success, image = vidcap.read()
  count = count+ 1