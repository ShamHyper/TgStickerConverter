import pylottie
from PIL import Image

tgs_file = input("Enter .tgs file full name (with dir): ")
output_prefix = input("Enter output filename (without extension): ")
fps = int(input("Output gif FPS: "))

print("Converting...")
output_file = f"{output_prefix}.gif"
pylottie.convertMultLottie2GIF([tgs_file], [output_file])

gif = Image.open(output_file)

frames = []
for frame in range(gif.n_frames):
    gif.seek(frame)
    new_frame = Image.new("RGBA", gif.size)
    new_frame.paste(gif)
    frames.append(new_frame)

output_speeded_up_file = f"{output_prefix}_{fps}_fps.gif"

duration = int(1000 / fps)

frames[0].save(
    output_speeded_up_file,
    save_all=True,
    append_images=frames[1:],
    loop=0,
    duration=duration,
    disposal=2
)

print("Done!")