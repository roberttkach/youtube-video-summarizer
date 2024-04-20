import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel


def recognize_speech(audio_file, language):
    SetLogLevel(0)

    model = Model(f"models/vosk-model-{language}")
    wf = wave.open(audio_file, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    with open('voice_to_text.txt', 'w', encoding='utf-8') as file:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                file.write(text + "\n")
