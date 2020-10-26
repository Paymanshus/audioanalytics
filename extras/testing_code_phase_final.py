import glob
import os
import soundfile

import keras
import librosa
import numpy as np
import pandas as pd

# from keras.models import model_from_json

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


def extract_feature(file_name, mfcc=True, chroma=True, mel=True, zero_crossr=True):
    X, sample_rate = librosa.load(
        os.path.join(file_name), res_type='kaiser_fast')
    if chroma:
        stft = np.abs(librosa.stft(X))
    result = np.array([])
    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(
            y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        result = np.hstack((result, mfccs))
    if chroma:
        chroma = np.mean(librosa.feature.chroma_stft(
            S=stft, sr=sample_rate).T, axis=0)
        result = np.hstack((result, chroma))
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(
            X, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mel))
    if zero_crossr:
        zero_crossr = np.mean(librosa.feature.zero_crossing_rate(X).T, axis=0)
        result = np.hstack((result, zero_crossr))

    return result


def pretrained_model_load():
    json_path = 'D:\\PyCharm Projects\\audioanalytics\\audioanalytics\\model.json'
    json_file = open(json_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = keras.models.model_from_json(loaded_model_json)
    loaded_model.load_weights(
        "D:\\PyCharm Projects\\audioanalytics\\audioanalytics\\model.h5")
    return loaded_model


def prediction():
    x, y = [], []
    print("Enter Path of the Audio File:")  # Save in variable instead of input
    # path = input()
    path = r"D:\PyCharm Projects\audioanalytics\03-01-03-01-02-01-16.wav"
    for file in glob.glob(path):
        file_name = os.path.basename(file)
        emotion = emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
    feature = extract_feature(file)
    # x.append(feature)
    # y.append(emotion) # y = emotion, not used directly
    # z = np.array(x)
    print("***MENU***")
    print("1. DataFrame with the values of Features")  # extract_feature
    print("2. Proceed with the Audio Analysis.")  # predict # + summary
    print("Enter your choice:")
    ch = input()
    if ch == "1":

        # z = pd.DataFrame(z)
        feature = pd.DataFrame(feature).T
        # print(z)
        print(feature)
    elif ch == "2":

        test_data = np.expand_dims(z, axis=2)

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
    else:

        print("WRONG CHOICE ENTERED. SORRY NO OUTPUT")


prediction()


"""
TODO: 
flow: path -> extract features -> df -> model load and run -> summary and predict
path save as variable, reduce possibilites of error
functionality, classes - emotions class 
menu change 
make less verbose - tmi displayed
summary change df display, check statsmodel
visualization -  pranav - mfcc - waveform - spectrogram - 
dependencies - tensorflow, librosa, numpy, pandas, soundfile, glob, os
package
"""
