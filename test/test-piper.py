


import subprocess
import os

PIPER_PATH = "/Users/jessica/Library/Python/3.14/bin/piper"   # <-- full path to piper
MODEL = "/Users/jessica/Documents/THB-TreeProject/SoftwareSetup/TalkingTree/models/de_DE-thorsten-high.onnx"
OUTPUT = "output.wav"

text = "Hallo! Hallo Hallo Dies ist ein Test der deutschen Stimme Thorsten mit Piper."

cmd = [
    PIPER_PATH,
    "--model", MODEL,
    "--output_file", OUTPUT
]

process = subprocess.Popen(
    cmd,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(text)

print("Piper finished.")
print("Output saved to:", OUTPUT)

if stderr:
    print("Errors:", stderr)