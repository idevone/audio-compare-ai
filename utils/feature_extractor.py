import librosa as lr
import numpy as np
import os


def extract_features(audio_path):
    y, sr = lr.load(audio_path)

    mfccs = lr.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = lr.feature.chroma_stft(y=y, sr=sr)
    tempo, beat_frames = lr.beat.beat_track(y=y, sr=sr)

    if len(tempo.shape) > 0:
        tempo = tempo[0]  # ! Берем первое (и единственное) значение, если tempo - массив

    # ! Исправляем размерности массивов, добавляя новое измерение к tempo
    feature_vector = np.concatenate((
        mfccs.mean(axis=1),
        chroma.mean(axis=1),
        np.array([tempo])
    ))

    return feature_vector
