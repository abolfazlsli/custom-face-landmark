import cv2 as cv 
import mediapipe as mp

mp_drowing = mp.solutions.drawing_utils
face_mp = mp.solutions.face_mesh
drawing_space = mp_drowing.DrawingSpec(
    thickness = 1 ,
    circle_radius= 1 , 
    color = (0, 0, 255)
)

cammer = cv.VideoCapture(0)

points = list(range(0,600))
with face_mp.FaceMesh( max_num_faces=2, min_detection_confidence=0.5,min_tracking_confidence=0.5) as face_mesh :
    while True : 
        frame , image = cammer.read()
        img = cv.cvtColor(image , cv.COLOR_BGR2RGB)
        img.flags.writeable = False
        result = face_mesh.process(img)
        img.flags.writeable = True
        img = cv.cvtColor(img , cv.COLOR_RGB2BGR)
        if result.multi_face_landmarks:
            for face_landmark in result.multi_face_landmarks:
                for point in range(0,len(face_landmark.landmark)):
                    targte = face_landmark.landmark[point]
                    h , w , _ = img.shape
                    x , y = int(targte.x * w) , int(targte.y * h)
                    # mp_drowing.draw_landmarks(
                    #     image = img,
                    #     landmark_list = face_landmark,
                    #     connections = face_mp.FACEMESH_TESSELATION,
                    #     landmark_drawing_spec = drawing_space,
                    #     connection_drawing_spec = drawing_space
                    # )
                    cv.circle(img, (x, y), 2, (0, 255, 0), -1)
                    # cv.putText(img, str(point), (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv.imshow("frames" ,  img)
        k = cv.waitKey(1)
        if k == ord("q") : 
            break

cammer.release()
cv.destroyAllWindows()
