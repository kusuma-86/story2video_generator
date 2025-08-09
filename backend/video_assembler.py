import os
import subprocess

def assemble_video(image_paths, audio_path, output_path="outputs/final_video.mp4"):
    os.makedirs("outputs", exist_ok=True)
    temp_list_file = "outputs/temp_list.txt"

    with open(temp_list_file, "w") as f:
        for img_path in image_paths:
            f.write(f"file '{os.path.abspath(img_path)}'\n")
            f.write("duration 4\n")

    slideshow_path = "outputs/temp_slideshow.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", temp_list_file,
        "-vsync", "vfr", "-pix_fmt", "yuv420p", slideshow_path
    ], check=True)

    subprocess.run([
        "ffmpeg", "-y", "-i", slideshow_path, "-i", audio_path,
        "-c:v", "copy", "-c:a", "aac", "-shortest", output_path
    ], check=True)

    return output_path
