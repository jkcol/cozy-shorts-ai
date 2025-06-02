import subprocess

def add_captions(video="final.mp4", srt="output.srt", output="captioned.mp4"):
    cmd = ["ffmpeg", "-y", "-i", video, "-vf", f"subtitles={srt}", output]
    subprocess.run(cmd)
    print("Captions added.")
