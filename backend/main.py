from fastapi import FastAPI, Request

app = FastAPI()
# ... rest of your code ...

from backend.generate_story import generate_scenes
from backend.image_gen import generate_image_with_background
from backend.video_assembler import assemble_video
from backend.tts_gen import generate_narration
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, safe for development
    allow_credentials=True,
    allow_methods=["*"],   # Allows all HTTP methods
    allow_headers=["*"],   # Allows all headers
)


app = FastAPI()

@app.post("/generate-video")
async def generate_video(request: Request):
    data = await request.json()
    story_text = data.get("story", "")
    
    scenes = generate_scenes(story_text)
    image_paths = [generate_image_with_background(scene) for scene in scenes]
    audio_path = generate_narration(scenes)
    video_path = assemble_video(image_paths, audio_path)

    return {"video_path": video_path}
