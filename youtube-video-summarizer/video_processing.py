from pytube import YouTube
from moviepy.editor import VideoFileClip


def download_video(link):
    youtube = YouTube(link)
    video = youtube.streams.first()
    video.download()
    return video.default_filename


def extract_audio(video_file):
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile("audio.wav")
    return "audio.wav"
