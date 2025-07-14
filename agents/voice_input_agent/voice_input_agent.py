import asyncio
import os
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from openai import OpenAI

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZmM0MDA0MC00NTVlLTQ3NjUtODdjZC0yZDFhNzY4YWI4YTQiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjRiMjFiOTQ3LTA1NzAtNGUyYi1iNjJmLTY0ODk2MDMxNDcyMyJ9.fbLz8OAwrCQ37T0YFUpHC5KCc7acw4gE90ll35PGFsY"
session = GenAISession(jwt_token=AGENT_JWT)

client = OpenAI(api_key="*")  # GenAI injects key

@session.bind(
    name="voice_input_agent",
    description="Explains complex medical diagnoses in simple English and other languages by taking audio as input."
)
async def voice_input_agent(
    agent_context: GenAIContext,
    user_input: Annotated[str, "Diagnosis text or uploaded MP3 UUID"]
):
    try:
        transcription = None

        # Convert UUID into .mp3 filename if needed
        if len(user_input) == 36 and "-" in user_input:
            user_input += ".mp3"

        # Check if it's an mp3
        if user_input.endswith(".mp3"):
            # ✅ Fallback: Assume mp3 is downloaded to current working dir or ./input_files/
            possible_paths = [
                os.path.join(".", user_input),
                os.path.join("./input_files", user_input),
                os.path.join("/mnt/data", user_input)  # for some environments
            ]
            mp3_path = next((p for p in possible_paths if os.path.isfile(p)), None)

            if not mp3_path:
                return {"error": f"📁 MP3 file '{user_input}' not found in expected locations."}

            with open(mp3_path, "rb") as audio_file:
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
                transcription = response.text
        else:
            # Plain text input
            transcription = user_input

        return {
            "transcription": transcription
        }

    except Exception as e:
        return {"error": f"❌ voice_input_agent failed: {str(e)}"}


async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
