from moviepy.editor import VideoFileClip, AudioFileClip

def combine_video_with_audio(video_path, audio_path, output_path):
    """Combine video and audio into a single file."""
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, codec="libx264")
    print(f"Final video with audio saved to {output_path}")
