import librosa
import os
import numpy as np


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
