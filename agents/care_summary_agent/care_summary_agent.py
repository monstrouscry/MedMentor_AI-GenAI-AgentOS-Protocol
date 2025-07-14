import asyncio
import os
import datetime
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

#AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1YjdlMzgwOS04OTM3LTQ2YTYtODI4OS02ZjExMmI1OTJlZDkiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjRiMjFiOTQ3LTA1NzAtNGUyYi1iNjJmLTY0ODk2MDMxNDcyMyJ9.paW2j1OPjfqIfU5flIRfQr8pL_93D7t2jBjdmTiTSeA" # noqa: E501

#AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4NDY5NzY3Ny02YmY2LTQwYmMtOTIyNC00YzRmNDFiZDU3NDYiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjRiMjFiOTQ3LTA1NzAtNGUyYi1iNjJmLTY0ODk2MDMxNDcyMyJ9.l8dr51ZnmEjxKEThBlmDZnXMQYzZSexAMNBKN3V1xOQ"  # replace this with your actual token
AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4YTg0Zjc3OS1jNDhhLTRmYjMtOTE3Zi1iODFlMjhhM2U3ZjEiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjRiMjFiOTQ3LTA1NzAtNGUyYi1iNjJmLTY0ODk2MDMxNDcyMyJ9.YeQjS39oXRaMymb1RFjCLS0Y7QM0fAlFNg7f4GhatKw"
session = GenAISession(jwt_token=AGENT_JWT)

# Register fonts
pdfmetrics.registerFont(TTFont("English", "Arial.ttf"))
pdfmetrics.registerFont(TTFont("Devanagari", "NotoSansDevanagari-Regular.ttf"))

def draw_multiline_text(c, x, y, text, font_name, font_size, max_width):
    c.setFont(font_name, font_size)
    lines = simpleSplit(text, font_name, font_size, max_width)
    for line in lines:
        c.drawString(x, y, line)
        y -= font_size + 3  # line height
    return y

@session.bind(
    name="care_summary_agent",
    description="Creates a PDF summary of diagnosis and explanations."
)
async def care_summary_agent(
    agent_context: GenAIContext,
    english: Annotated[str, "English explanation"],
    hindi: Annotated[str, "Optional Hindi translation"] = None,
    marathi: Annotated[str, "Optional Marathi translation"] = None,
    spanish: Annotated[str, "Optional Spanish translation"] = None
):
    output_path = "patient_summary.pdf"
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    x_margin = 50
    y = height - 50

    # Title
    c.setFont("English", 16)
    c.drawCentredString(width / 2, y, "■ Patient Summary Report")
    y -= 30

    # Date
    c.setFont("English", 12)
    c.drawString(x_margin, y, f"Date: {datetime.date.today()}")
    y -= 30

    # English section
    c.setFont("English", 12)
    c.drawString(x_margin, y, "English Explanation:")
    y -= 20
    y = draw_multiline_text(c, x_margin, y, english, "English", 12, width - 100)

    # Hindi section
    if hindi:
        y -= 20
        c.setFont("Devanagari", 12)
        c.drawString(x_margin, y, "हिंदी अनुवाद:")
        y -= 20
        y = draw_multiline_text(c, x_margin, y, hindi, "Devanagari", 12, width - 100)

    # Marathi section
    if marathi:
        y -= 20
        c.setFont("Devanagari", 12)
        c.drawString(x_margin, y, "मराठी भाषांतर:")
        y -= 20
        y = draw_multiline_text(c, x_margin, y, marathi, "Devanagari", 12, width - 100)

    # Spanish section
    if spanish:
        y -= 20
        c.setFont("English", 12)
        c.drawString(x_margin, y, "Spanish Translation:")
        y -= 20
        y = draw_multiline_text(c, x_margin, y, spanish, "English", 12, width - 100)

    try:
        c.save()
        return {"message": f"📄 PDF successfully saved as {output_path}"}
    except Exception as e:
        return {"error": f"❌ PDF output error: {str(e)}"}

# Start the agent loop
async def main():
    print("Care Summary Agent started...")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
