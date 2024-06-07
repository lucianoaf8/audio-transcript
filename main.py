import os
import whisper

model = whisper.load_model("base")

input_dir = r"C:\Users\Luciano\Documents\Projects\audio-transcript\to_transcript"
output_dir = r"C:\Users\Luciano\Documents\Projects\audio-transcript\transcripted"

# Ensure directories exist
if not os.path.exists(input_dir):
    os.makedirs(input_dir)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".m4a"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".txt")

        result = model.transcribe(input_path)
        with open(output_path, "w") as f:
            f.write(result["text"])

print("Transcription complete.")
