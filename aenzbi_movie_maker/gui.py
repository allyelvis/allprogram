import tkinter as tk
from tkinter import filedialog
from video_processing import apply_grayscale, add_text_overlay, trim_video, save_video

def open_file():
    filename = filedialog.askopenfilename()
    if filename:
        process_video(filename)

def process_video(video_path):
    # Example of applying grayscale to the video
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = apply_grayscale(frame)
        frames.append(gray_frame)
    cap.release()
    
    save_video(frames, "output_grayscale.avi")

def create_gui():
    root = tk.Tk()
    root.title("Aenzbi Movie Maker")

    open_button = tk.Button(root, text="Open Video File", command=open_file)
    open_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
