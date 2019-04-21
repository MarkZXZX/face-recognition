import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)
#video_capture.set(3,1366) #设置分辨率
#video_capture.set(4,1920)
#video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,1280)
Liu_img= face_recognition.load_image_file("Liu.jpg")
#hurenyu_img = face_recognition.load_image_file("renyu.jpg")
Liu_face_encoding = face_recognition.face_encodings(Liu_img)[0]

Lin_img = face_recognition.load_image_file("Lin.jpg")
Lin_face_encoding = face_recognition.face_encodings(Lin_img)[0]



known_face_encodings = [
    Liu_face_encoding,
    Lin_face_encoding,

]

known_face_names = [
    "Liu_yifei",
    "Lin_yuner",

]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    if process_this_frame:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unkown"
            if True in matches:
                #                 print(len(matches))
                first_match_index = matches.index(True)
                #                 print(first_match_index)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),  2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left+6, bottom-6), font, 1.0, (255, 255, 255), 1)
    #cv2.resizeWindow("Video", 1080, 720);
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()