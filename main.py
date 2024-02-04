from deepface import DeepFace
import cv2


def analyze_faces(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Analyze faces using DeepFace
    try:
        result = DeepFace.analyze(img_path=image_path, actions=[
                                  'emotion', 'age', 'gender', 'race'])
        print("Facial Analysis Result:")
        print(result)
    except Exception as e:
        print("Error analyzing faces:", str(e))


if __name__ == "__main__":
    # Replace 'path/to/your/image.jpg' with the actual path to your image file
    image_path = '/images/musk.jpg'

    analyze_faces(image_path)
