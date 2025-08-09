import os
import random
from PIL import Image
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")
pipe.to("cpu")  # Use "cuda" if GPU is available

def pick_random_background(background_dir="assets/backgrounds"):
    all_images = []
    for root, _, files in os.walk(background_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                all_images.append(os.path.join(root, file))
    if not all_images:
        return None
    return random.choice(all_images)

def generate_image_with_background(scene_text, background_dir="assets/backgrounds", output_dir="outputs/images"):
    background_path = pick_random_background(background_dir)
    if background_path:
        background = Image.open(background_path).convert("RGBA")
    else:
        background = Image.new("RGBA", (512, 512), (255, 255, 255, 255))  # fallback white

    prompt = f"Character and objects for scene: {scene_text}"
    generated = pipe(prompt).images[0].convert("RGBA")

    background = background.resize(generated.size)
    combined = Image.alpha_composite(background, generated)

    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{hash(scene_text)}.png")
    combined.convert("RGB").save(filename)
    return filename
