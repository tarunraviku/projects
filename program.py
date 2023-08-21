import speech_recognition as sr
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_filename): # takes mp3 file name as input
    sound = AudioSegment.from_mp3(mp3_filename)
    wav_filename = mp3_filename.replace(".mp3", ".wav")
    sound.export(wav_filename, format="wav")
    return wav_filename

def mp3_to_text(mp3_filename):  # takes mp3 file name as input
    wav_filename = convert_mp3_to_wav(mp3_filename)

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_filename) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Failed to understand audio, try again")
        return None
    

if __name__ == "__main__":
    mp3_filename = "pranusample.mp3"
    text = mp3_to_text(mp3_filename)
    if text is not None:
        print("MP3 Transcription Below:")
        print(text)
