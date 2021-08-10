import cv2
import glob

dir = "via-tfsclassification_beta/val/"
for i in range(7):
    filenames = glob.glob(dir + str(i) +"/" + "*.jpg")
    for f in filenames:
        imagedata = cv2.imread(f)
        if imagedata.shape[0] != 128 or imagedata.shape[1] != 128:
            # imagedata = cv2.resize(imagedata,(128,128))
            # cv2.imwrite(f,imagedata)
            # cv2.waitKey(10)
            print(f)