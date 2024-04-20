from pydub import AudioSegment


def convert_to_mono(audio_file):
    sound = AudioSegment.from_file(audio_file)
    sound = sound.set_channels(1)
    mono_audio_file = "output.wav"
    sound.export(mono_audio_file, format="wav")
    return mono_audio_file
