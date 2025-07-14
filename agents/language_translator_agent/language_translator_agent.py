import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from openai import OpenAI

client = OpenAI(api_key="")  # GenAI injects key

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4YTg0Zjc3OS1jNDhhLTRmYjMtOTE3Zi1iODFlMjhhM2U3ZjEiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjRiMjFiOTQ3LTA1NzAtNGUyYi1iNjJmLTY0ODk2MDMxNDcyMyJ9.YeQjS39oXRaMymb1RFjCLS0Y7QM0fAlFNg7f4GhatKw" # noqa: E501
session = GenAISession(jwt_token=AGENT_JWT)


@session.bind(
    name="language_translator_agent",
    description="Translates medical explanations into local languages."
)
async def language_translator_agent(
    agent_context: GenAIContext,
    english_text: Annotated[str, "Text to translate"]
):
    translations = {}

    for lang in ["Hindi", "Marathi", "Spanish"]:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Translate the following into {lang}:"},
                {"role": "user", "content": english_text}
            ]
        )
        translations[lang] = response.choices[0].message.content.strip()

    return translations

async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
