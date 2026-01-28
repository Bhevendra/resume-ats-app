from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_resume(candidate_text: str, jd_text: str) -> str:
    prompt = f"""
You are an expert ATS resume writer.

Candidate Experience:
{candidate_text}

Job Description:
{jd_text}

Rules:
- ATS friendly
- No fabrication
- Quantified bullets
- 1–2 pages
- Use strong action verbs

Return clean, structured resume text.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
