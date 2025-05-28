# Cargar modelos desde carpeta local
face_recognition.api.face_recognition_model_location = lambda: "models/dlib_face_recognition_resnet_model_v1.dat"
face_recognition.api.pose_predictor_model_location = lambda: "models/shape_predictor_68_face_landmarks.dat"
face_recognition.api.cnn_face_detector_model_location = lambda: "models/mmod_human_face_detector.dat"  # opcional

