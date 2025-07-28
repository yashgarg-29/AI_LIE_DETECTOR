import cv2
import mediapipe as mp

def detect_face_lie():
    mp_face = mp.solutions.face_mesh
    face_mesh = mp_face.FaceMesh()

    cap = cv2.VideoCapture(0)
    result = 0  # 0 = Truth, 1 = Lie (stress detected)
    frame_count = 0
    eyebrow_movements = 0

    while frame_count < 30:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb)

        if output.multi_face_landmarks:
            for face_landmarks in output.multi_face_landmarks:
                # Track eyebrow movement (landmarks 65, 295 near eyebrows)
                left_brow = face_landmarks.landmark[65]
                right_brow = face_landmarks.landmark[295]

                if left_brow.y < 0.3 or right_brow.y < 0.3:
                    eyebrow_movements += 1

        frame_count += 1
        cv2.imshow("Face Scan (Press Q)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # If many eyebrow movements, assume stress/lie
    if eyebrow_movements > 10:
        result = 1  # Lie
    return result