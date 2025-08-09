import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_scenes(story_text):
    prompt = f"Break this story into 4 visual scenes:\n\n{story_text}\n\nReturn as:\nScene 1: ... Scene 2: ..."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    result = response['choices'][0]['message']['content']
    scenes = [line.split(":", 1)[1].strip() for line in result.split('\n') if line.strip().startswith("Scene")]
    return scenes
