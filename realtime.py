# staircase detection using opencv techniques

# importing the necessary packages
import numpy as np
import cv2
from math import sqrt


# declaring variable to count the number of stairs
i = 0
# declaring variable to get length of line
b = 0
# declaring variable to check length of a set
c = 0
# declaring list to store length of lines
a = []
cap = cv2.VideoCapture('stair.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    frame=cv2.rotate(frame,cv2.cv2.ROTATE_90_CLOCKWISE)

    # convert to grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # perform edge detection
    edges = cv2.Canny(grayscale, 50, 150)

    # detect lines in the image using hough lines technique
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 60, np.array([]), minLineLength=60, maxLineGap=5)

    # trying block to check if no any line in image
    try:

        # check if lines are there
        if lines in lines is not None:

             # taking each line for testing the parameters
             for line in lines:

                 # taking points from each line for testing
                 for x1, y1, x2, y2 in line:

                    # checking for parallel lines
                    if (y2 - y1) / (x2 - x1) in np.linspace(0, 0.5, 1000000):

                         b = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                         a.append(b)
                         c = len(set(a))
                         i = i + 1

                         # checking if lines are of same length
                         # checking for sufficient numbers of lines
                         if (c != 1) and (4 < i < 20):
                            cv2.line(frame, (x1, y1), (x2, y2), (20, 220, 20), 2)
        if (c != 1) and (4 < i < 20):
            k = str(i)
            font = cv2.FONT_HERSHEY_COMPLEX
            org = (20, 160)
            color = (255, 0, 0)
            fontScale = 0.5
            thickness = 1
            cv2.putText(frame, k + ' stairs', org, font, fontScale, color, thickness)






    # if no line is detected so no chance for stairs
    except Exception:
        # to do nothing if there is no any line in image
        pass

    cv2.imshow('frame', frame)
    if cv2.waitKey(10 & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
