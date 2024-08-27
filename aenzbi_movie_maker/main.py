import argparse
from video_processing import trim_video, apply_grayscale, save_video
from audio_processing import combine_video_with_audio

def main():
    parser = argparse.ArgumentParser(description="Aenzbi Movie Maker")
    
    parser.add_argument('--input', type=str, help="Path to the input video file", required=True)
    parser.add_argument('--output', type=str, help="Path to save the output video file", required=True)
    parser.add_argument('--effect', type=str, choices=['grayscale'], help="Apply a video effect", default=None)
    parser.add_argument('--start_frame', type=int, help="Start frame for trimming", default=0)
    parser.add_argument('--end_frame', type=int, help="End frame for trimming", default=None)
    parser.add_argument('--text', type=str, help="Text to overlay on video", default=None)
    parser.add_argument('--audio', type=str, help="Path to an audio file to add", default=None)
    
    args = parser.parse_args()

    # Apply selected effect
    if args.effect == 'grayscale':
        cap = cv2.VideoCapture(args.input)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            processed_frame = apply_grayscale(frame)
            if args.text:
                processed_frame = add_text_overlay(processed_frame, args.text)
            frames.append(processed_frame)
        cap.release()
        save_video(frames, args.output)

    # Trim the video if start and end frames are specified
    if args.start_frame is not None and args.end_frame is not None:
        trim_video(args.input, args.start_frame, args.end_frame, args.output)

    # Combine video with audio if an audio file is provided
    if args.audio:
        combine_video_with_audio(args.input, args.audio, args.output)

if __name__ == "__main__":
    main()
