import os


def cleanup_files(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Удален файл: {file}")
        else:
            print(f"Файл не найден: {file}")


def cleanup():
    temp_files = [
        "audio.wav",
        "output.wav",
        "voice_to_text.txt"
    ]
    cleanup_files(temp_files)

    video_files = [f for f in os.listdir() if f.endswith(".mp4")]
    cleanup_files(video_files)
