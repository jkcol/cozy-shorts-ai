import os
import subprocess

def create_video(background="assets/backgrounds/bg.mp4", audio="voice.mp3", output="final.mp4"):
    cmd = [
        "ffmpeg", "-y", "-i", background, "-i", audio,
        "-c:v", "copy", "-c:a", "aac", "-shortest", output
    ]
    subprocess.run(cmd)
    print("Video created.")
