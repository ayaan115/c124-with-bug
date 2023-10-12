# import the opencv library
import cv2
import tensorflow as tf

model = tf.keras.models.load_model("keras_model.h5")
  
# define a video capture object
video = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame by frame
    check, frame = video.read()

    prediction = model.predict(frame)
    print("Prediction: ", prediction)
  
    # Display the resulting frame
    cv2.imshow('Result', frame)
      
    # Quit window with spacebar
    key = cv2.waitKey(1)
    
    if key == 32:
        break
  
# After the loop release the cap object
video.release()

# Destroy all the windows
cv2.destroyAllWindows()