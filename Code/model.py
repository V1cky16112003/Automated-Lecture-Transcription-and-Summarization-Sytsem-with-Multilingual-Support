import whisper

def save_transcription_result(result, file_path):
    with open(file_path, 'w') as f:
        f.write(result["text"])

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe("/Users/vigneshram/Downloads/1.wav", fp16=False)

# Specify the output file path
file_path = "/Users/vigneshram/Documents/code/transcription.txt"

# Save the transcription result to the specified file
save_transcription_result(result, file_path)
print(f"Transcription saved to file: {file_path}")