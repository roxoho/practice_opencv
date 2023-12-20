import os, cv2
import numpy as np

original = cv2.imread("./1.png")
filled = cv2.imread("./2.png")

original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
filled_gray = cv2.cvtColor(filled, cv2.COLOR_BGR2GRAY)

MAX_FEATURES = 1000
orb = cv2.ORB_create(MAX_FEATURES)
keypoints_original, descriptors_original = orb.detectAndCompute(original_gray, None)
keypoints_filled, descriptors_filled = orb.detectAndCompute(filled_gray, None)

#keypoints
#cv2.drawKeypoints(original, keypoints_original, original, color=(0, 255, 0), flags=0)
#cv2.drawKeypoints(filled, keypoints_filled, filled, color=(0, 255, 0), flags=0)

#matching

matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = matcher.match(descriptors_original, descriptors_filled, None)

# Define a custom sorting key based on the 'distance' attribute of cv2.DMatch
matches = sorted(matches, key=lambda x: x.distance)


# Now you can proceed with your slicing
matches = matches[:int(len(matches) * 0.1)]


im_matches=cv2.drawMatches(original, keypoints_original, filled, keypoints_filled, matches, filled, flags=2)

#cv2.imshow("matches", im_matches)
#homography
points_original = np.zeros((len(matches), 2), dtype=np.float32)
points_filled = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points_original[i, :] = keypoints_original[match.queryIdx].pt
    points_filled[i, :] = keypoints_filled[match.trainIdx].pt

h, mask = cv2.findHomography(points_filled, points_original, cv2.RANSAC)

#warp
height, width, channels = original.shape
filled_warped = cv2.warpPerspective(filled, h, (width, height))

cv2.imshow("original", original)
cv2.imshow("filled_warped", filled_warped)


#cv2.imshow("original", original)
#cv2.imshow("filled", filled)
cv2.waitKey(0)