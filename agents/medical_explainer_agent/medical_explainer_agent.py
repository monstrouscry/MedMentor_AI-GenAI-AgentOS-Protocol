import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from openai import OpenAI

# ✅ Use GenAI’s internal API key by passing `api_key=None`
client = OpenAI(api_key="")


AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlNzcxNzQ4NC1hZjVmLTRmNjgtYTJhZC0zMDQ1M2Q4NTEyYzYiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjRiMjFiOTQ3LTA1NzAtNGUyYi1iNjJmLTY0ODk2MDMxNDcyMyJ9.feRDu205bvtaDMOM19W5ItAcgV7q5kyEc4sjgtdu-_U" # noqa: E501
session = GenAISession(jwt_token=AGENT_JWT)


@session.bind(
    name="medical_explainer_agent",
    description="Explains complex medical diagnoses in simple English."
)
async def medical_explainer_agent(
    agent_context: GenAIContext,
    content: Annotated[str, "Diagnosis input, e.g. 'Stage 1 NSCLC'"]
):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a compassionate medical assistant. You explain medical diagnoses using simple, friendly language. "
                    "Avoid jargon, never give false hope, and clearly note that this is not a substitute for a doctor's advice."
                )
            },
            {
                "role": "user",
                "content": f"Explain this diagnosis for a patient: {content}"
            }
        ]
    )

    explanation = response.choices[0].message.content.strip()
    return {"explanation": explanation}

async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
