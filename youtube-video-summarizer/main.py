import video_processing
import audio_processing
import speech_recognition
import text_summarization
from cleanup import cleanup
from constants import LINK, LANGUAGE


def main():
    video_file = video_processing.download_video(LINK)
    audio_file = video_processing.extract_audio(video_file)
    mono_audio_file = audio_processing.convert_to_mono(audio_file)

    speech_recognition.recognize_speech(mono_audio_file, LANGUAGE)

    text_summarization.summarize_text('voice_to_text.txt', 'result.txt')
    cleanup()


if __name__ == '__main__':
    main()
