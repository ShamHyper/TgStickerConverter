import lottie
from PIL import Image
from moviepy.editor import ImageSequenceClip
import os

def tgs_to_gif(tgs_file, output_gif, frame_duration=50):
    with open(tgs_file, 'rb') as f:
        animation = lottie.parsers.tgs.parse_tgs(f.read())

    temp_dir = "frames"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    frames = []
    for i in range(animation.frame_count):
        frame = animation.render(i)
        frame_image = Image.fromarray(frame)
        frame_path = os.path.join(temp_dir, f"frame_{i:03d}.png")
        frame_image.save(frame_path)
        frames.append(frame_path)

    clip = ImageSequenceClip(frames, fps=1000 // frame_duration)
    clip.write_gif(output_gif)

    for frame in frames:
        os.remove(frame)
    os.rmdir(temp_dir)

tgs_file = input("Enter .tgs file full name (with dir): ")
output_gif = input("Enter .gif output filename (without extension): ") + ".gif"

tgs_to_gif(tgs_file, output_gif)