import os
import time
import logging
from pytube import YouTube
from moviepy.editor import AudioFileClip

from utils.feature_extractor import extract_features


def download_video(video_url):
    logging.log(logging.INFO, "Downloading video from URL: " + video_url)
    yt = YouTube(video_url)
    title = yt.title
    author = yt.author
    yt.streams.filter(only_audio=True).first().download(filename='temporary.mp4', output_path='../data/')
    logging.log(logging.INFO, "Download completed")
    return title, author


def convert_to_wav(url):
    title, author = download_video(url)
    path_to_file = '../data/temporary.mp4'

    video_clip = AudioFileClip(path_to_file)
    audio_clip = video_clip.subclip(0, video_clip.duration)
    output_name = '../data/audios/' + title
    audio_clip.write_audiofile(output_name + '.wav', codec='pcm_s16le')

    audio_clip.close()
    video_clip.close()

    logging.log(logging.INFO, "Audio file created")
    os.remove(path_to_file)
    logging.log(logging.INFO, "Conversion to mp3 completed")

    print(extract_features(os.path.join('..', 'data', 'audios', f'{title}.wav')))


convert_to_wav("https://music.youtube.com/watch?v=A8xY6bMRocY&feature=shared")
