import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

audio_file = "audio.wav"
transcription_file = "prompt.txt"

with open(audio_file, "rb") as file:
    transcription = client.audio.transcriptions.create(
      file=(audio_file, file.read()),
      model="whisper-large-v3",
      response_format="verbose_json",
    )
    
    with open(transcription_file, "w") as output_file:
        output_file.write(transcription.text)
    
    print("Transcription saved to transcription_files folder")