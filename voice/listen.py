

import os
import subprocess
import time
import traceback
from typing import Callable
from pydub import AudioSegment
import speech_recognition as sr


def resample_wav_to_16khz(input_file, output_file):
    audio = AudioSegment.from_wav(input_file)
    audio = audio.set_frame_rate(16000)
    audio.export(output_file, format="wav")

def save_audio_to_wav(audio_data, directory="recordings"):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate a timestamped filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"audio_{timestamp}.wav"
    file_path = os.path.join(directory, filename)

    # Save the audio data as a .wav file
    with open(file_path, "wb") as f:
        f.write(audio_data.get_wav_data())

    print(f"Audio saved as {file_path}")
    resample_wav_to_16khz(file_path, file_path)
    return file_path

def run_program_and_capture_output(command):
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output.strip()

def run_whisper(path_to_file):
    return run_program_and_capture_output(["./whisper.cpp/main", "-m", "./whisper.cpp/models/ggml-base.en.bin", "-f" ,path_to_file, "-nt" ,"-t", "8"])

def listen(callback: Callable):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Calibrating...')
        r.adjust_for_ambient_noise(source, duration=2)
        while(1):
            input("Press any key to STT...")
            text = ''
            print('listening now...')
            try:
                audio = r.listen(source, timeout=20, phrase_time_limit=30)
                audio_file = save_audio_to_wav(audio)
                recognized = run_whisper(audio_file)
                print("Recognized:")
                print(recognized)
                callback(recognized)
            except Exception as e:
                traceback.print_exc()
                unrecognized_speech_text = f'Sorry, I didn\'t catch that. Exception was: {e}s'
                text = unrecognized_speech_text

            print(text)
