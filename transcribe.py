import os
import warnings
import whisper
from datetime import timedelta

model = whisper.load_model("base")

# Suppress FP16 warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Define input and output directories relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "data/input")
output_dir = os.path.join(script_dir, "data/output")

# Ensure directories exist
if not os.path.exists(input_dir):
    os.makedirs(input_dir)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def format_time(seconds):
    td = timedelta(seconds=seconds)
    minutes, seconds = divmod(td.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

files = [f for f in os.listdir(input_dir) if f.endswith(".m4a")]
total_files = len(files)

for i, filename in enumerate(files):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".txt")

    print(f"Processing file {i + 1}/{total_files}: {filename}")
    result = model.transcribe(input_path)
    with open(output_path, "w") as f:
        for segment in result['segments']:
            start = format_time(segment['start'])
            end = format_time(segment['end'])
            text = segment['text']
            f.write(f"[{start} - {end}] {text}\n")

print("Transcription complete.")
