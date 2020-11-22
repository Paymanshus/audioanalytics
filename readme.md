# AudioAnalytics Package Version(Release v0.1.1)

## Overview

The audioanalytics package provides functions for easy extraction of audio features from a given audio file, which can be used in modeling or other visualisations as per the user's requirements. It also has functionality for detecting emotions in the audio sample provided by the user(given a sample of a human voice), giving a prediction probability of various possible emotions predicted.


This is a development build, current active version is at https://pypi.org/project/audioanalytics/ (https://github.com/pranavkotak8/audioanalytics)

-----------------------------------------------

## Usage Guidelines

1. Importing the Package:

`import audioanalytics`

2. Extracting the feature values from the audio file.
Enter file path first.


`file=r'path goes here'
from audioanalytics import extract_feature
extract_feature(file)`

3. For Model_load

`from audioanalytics import model_load
model_load()`

4. For Prediction

`from audioanalytics import predict
file_path=r'path goes here'
predict(file_path)`

5. For Summary Report

`from audioanalytics import summary
file_path=r'path goes here'
summary(file_path)`

-------------------------------------------------------


## Components of the AudioAnalytics Package:

1) Extract Feature - It will return the feature values in a Dataframe.
2) Model_Load - It loads the model from backend.
3) Predict - Predicts the Emotion by conducting the analysis of the provided audio.
4) Summary Report - A report where probabilities are displayed of 4 Emotions.


NOTE : Support for other file formats will be added in later versions
