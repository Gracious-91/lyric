print("Running lyric video script...")

from moviepy.editor import *

# Load the audio file
audio = AudioFileClip("song.mp3")
duration = audio.duration

# Load and resize the background image
background = ImageClip("background.jpg").resize((1280, 720)).set_duration(duration)

# List to hold all text (lyric) clips
text_clips = []

# Open and read the lyrics file
with open("lyrics.txt", "r") as file:
    for line in file:
        # Split each line: start time, end time, and text
        start, end, text = line.strip().split(",", 2)
        start_time = float(start)
        end_time = float(end)
        clip_duration = end_time - start_time

        # Create the text clip
        clip = TextClip(
            text,
            fontsize=50,
            color='white',
            size=(1280, 720),
            font="Arial",
            method='caption'
        )

        # Apply fade-out and timing
        clip = (clip.set_start(start_time)
                    .set_duration(clip_duration)
                    .set_position('bottom')
                    .fadeout(1))  # 1 second fade out at the end

        # Add to list
        text_clips.append(clip)

# Combine the background and all text clips
final_video = CompositeVideoClip([background, *text_clips])
final_video = final_video.set_audio(audio)

# Export the final video
final_video.write_videofile("lyric_video_with_fadeout.mp4", fps=24)
