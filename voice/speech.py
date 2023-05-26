import os
from elevenlabs import generate, stream

elevenlabs_api_key = os.getenv("ELEVEN_API_KEY")


def speak(text, voice = "7e2p09M5txOQndhE2bMk"):
    audio_stream = generate(
        text=text,
        stream=True,
        api_key=elevenlabs_api_key, 
        voice=voice
    )

    stream(audio_stream)
