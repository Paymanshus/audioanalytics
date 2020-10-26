import glob
import os
import numpy as np
import pandas as pd
import keras

from .features import extract_feature
from .model import pretrained_model_load

emotions = {
    '01': 'neutral',
    '02': 'calm',
    '03': 'happy',
    '04': 'sad',
    '05': 'angry',
    '06': 'fearful',
    '07': 'disgust',
    '08': 'surprised'
}

observed_emotions = ['calm', 'happy', 'fearful', 'disgust']


def summary():
    print("Summary function will go here")


def predict(file_name):
    feature = pd.DataFrame(extract_feature(file_name)).T

    test_data = np.expand_dims(feature, axis=2)

    loaded_model = pretrained_model_load()
    loaded_model.compile(loss=keras.losses.categorical_crossentropy,
                         optimizer=keras.optimizers.Adadelta(),
                         metrics=['accuracy'])

    pred = loaded_model.predict_classes(test_data)

    if pred[0] == 0:
        print("THE RESULT OF THE AUDIO ANALYSIS IS: CALM")
    elif pred[0] == 1:
        print("THE RESULT OF THE AUDIO ANALYSIS IS: HAPPY")
    elif pred[0] == 2:
        print("THE RESULT OF THE AUDIO ANALYSIS IS: FEARFUL")
    else:
        print("THE RESULT OF THE AUDIO ANALYSIS IS: DISGUST")
