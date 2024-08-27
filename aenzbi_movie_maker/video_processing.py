import cv2

def apply_grayscale(frame):
    """Apply a grayscale effect to the frame."""
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def add_text_overlay(frame, text, position=(50, 50), font=cv2.FONT_HERSHEY_SIMPLEX, 
                     font_scale=1, color=(255, 255, 255), thickness=2):
    """Add text overlay to the frame."""
    return cv2.putText(frame, text, position, font, font_scale, color, thickness)

def trim_video(video_path, start_frame, end_frame, output_path):
    """Trim video from start_frame to end_frame."""
    cap = cv2.VideoCapture(video_path)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), 20.0, 
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret or frame_count > end_frame:
            break
        if frame_count >= start_frame:
            out.write(frame)
        frame_count += 1
    
    cap.release()
    out.release()
    print(f"Trimmed video saved to {output_path}")

def save_video(frames, output_path, fps=20.0, resolution=(640, 480)):
    """Save a sequence of frames to a video file."""
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, resolution)
    for frame in frames:
        out.write(frame)
    out.release()
    print(f"Video saved to {output_path}")
