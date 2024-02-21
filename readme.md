# Emotion Recognition Project

## Overview

This project aims to develop a deep learning model for emotion recognition in images. The model is trained on a dataset containing images of facial expressions corresponding to different emotions, including anger, contempt, disgust, fear, happiness, sadness, and surprise.

## Project Structure

The project repository contains the following files and directories:

- **train_model.ipynb**: Jupyter Notebook containing the code for loading the dataset, preprocessing images, building, training, and evaluating the emotion recognition model.
- **emotion_recognition_model.h5**: Pre-trained model file saved in HDF5 format.

- **emotion_recognition_model.keras**: Pre-trained model file saved in Keras native format.

- **utils.py**: Utility functions for loading and preprocessing images, as well as decoding predicted emotion labels.

- **requirements.txt**: List of Python dependencies required to run the project.

- **/dataset**: Directory containing the training dataset, organized into subdirectories for each emotion category.

## Usage

To train the emotion recognition model:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Open and execute the `train_model.ipynb` notebook in a Jupyter environment.

To predict emotions from local images:

1. Ensure that the pre-trained model file `emotion_recognition_model.h5` is available in the project directory.
2. Use the `predict_emotion.py` script by providing the path to the local image as an argument.

Example usage:

```bash
python predict_emotion.py /path/to/local/image.jpg
```

## Dependencies

- Python (>=3.6)
- TensorFlow (>=2.0)
- Keras (>=2.0)
- NumPy
- Matplotlib
- OpenCV

## Credits

This project is developed by **Saqlen Raza Mehdi** as part of **Final Year Research Project**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
