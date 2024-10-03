import threading
import cv2 

from deepface import DeepFace


#from deepface import DeepFace

#capture is physical camera
capture = cv2.VideoCapture(0)  #first parameter (0) -- how many cameras you have, 2nd parameter - source 
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False
left_eye = None
right_eye = None

def detection(image):
    global face_match
    global left_eye
    global right_eye

    print("Ran")
    try:   #try/except if no face detected, it returns "No face detected" instead of error
        result = DeepFace.verify (
            image,
            img2_path = "sarasmajic.jpg" )
        
        face_match = (result["verified"])
        print(face_match)

        left_eye = (result["facial_areas"]["img1"]["left_eye"])
        right_eye = (result["facial_areas"]["img1"]["right_eye"])

    except ValueError:
        #cv2.putText(image, "NO FACE DETECTED!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        face_match = False
        #print("No face detected!")



while True: 
    counter += 1

    result, image = capture.read()  #capture.read returns tuple, first element is result(TRUE if successfully taken the picture, either false), second element is physical picture

    #cv2.waitKey(0) #0 is any key, pressing it means moving onto the next taken picture

    #cv2.imwrite("og_image.jpg", image)

    #reference_img = cv2.imread("sarasmajic.jpg")

    if counter % 50 == 1:
       # result = detection(image)   #result is true/false
        threading.Thread(target=detection, args=(image.copy(),)).start() 

    #print(face_match)
    if face_match == True:
        cv2.putText(image, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    else:
        cv2.putText(image, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        
    cv2.circle(image, left_eye, 50, (150, 0, 0), 5)
    cv2.circle(image, right_eye, 50, (150, 0, 0), 5)
    if left_eye != None:
        cv2.line(image, (left_eye[0]-50, left_eye[1]), (right_eye[0] + 50, right_eye[1]), (150, 0, 0), 5)

    cv2.imshow("slika",image) #imshow displays the picture, "slika" is the name of the window


    key = cv2.waitKey(1)
    if key == ord("q"):
        break

    #if cv2.waitKey(0) == ord("q"):#if q pressed, it breaks out of loop and destroys the GUI window
        #cv2.imwrite("og_image.jpg", image)
    #    break

cv2.destroyAllWindows()


