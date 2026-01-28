from fastapi import APIRouter, UploadFile, Form, HTTPException
import traceback

from app.services.pdf_parser import extract_pdf_text
from app.services.jd_parser import fetch_jd_text
from app.services.resume_generator import generate_resume

router = APIRouter()

@router.post("/generate")
async def generate_resume_api(
    pdf: UploadFile,
    jd_url: str = Form(...)
):
    try:
        candidate_text = extract_pdf_text(pdf.file)

        jd_text = fetch_jd_text(jd_url)
        if not jd_text or len(jd_text.strip()) < 50:
            raise ValueError("JD text could not be extracted")

        resume_text = generate_resume(candidate_text, jd_text)

        return {
            "resume_text": resume_text
        }

    except Exception as e:
        print("🔥 ERROR IN /api/generate 🔥")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
