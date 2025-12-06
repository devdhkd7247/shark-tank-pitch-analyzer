import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def analyze_content(audio_file):
    transcript = "Sample transcript (replace w/ Whisper later)"

    prompt = f"""
    Grade this pitch content on:
    - Problem Clarity
    - Market Opportunity
    - Revenue Model
    - Competition Awareness

    Transcript: {transcript}

    Give:
    1) Score (0-100)
    2) Brief Summary
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    msg = response.choices[0].message.content
    score = 75

    return transcript, score, msg
