import cv2

video_name = "작사가 김이나 초대석.mp4"
vidcap = cv2.VideoCapture("./youtube/{}".format(video_name))
success, image = vidcap.read()
count = 0

while success:
    cv2.imwrite("./output/%06d.jpg" % count, image)
    success, image = vidcap.read()
    print("Read a new frame :", success)
    count += 1

print("finish converting {}".format(video_name))