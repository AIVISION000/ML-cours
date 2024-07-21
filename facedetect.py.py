import cv2
import face_recognition

# فتح الكاميرا
video_capture = cv2.VideoCapture(0)

while True:
    # التقاط إطار واحد من الفيديو
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to grab frame")
        break

    # تحويل الإطار من BGR إلى RGB لأن OpenCV تستخدم BGR و face_recognition تستخدم RGB
    rgb_frame = frame[:, :, ::-1]

    # العثور على جميع الوجوه في الإطار الحالي
    face_locations = face_recognition.face_locations(rgb_frame)

    # رسم مستطيل حول كل وجه
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # عرض الإطار مع المستطيلات
    cv2.imshow('Video', frame)

    # الضغط على مفتاح 'q' للخروج
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# إطلاق الكاميرا وإغلاق جميع النوافذ
video_capture.release()
cv2.destroyAllWindows()
