from fastapi import FastAPI, UploadFile, File, HTTPException
import fitz
from pydantic import BaseModel, field_validator

app = FastAPI(title='Minidoc AI')

class QuestionRequest(BaseModel):
    question: str

    @field_validator('question')
    @classmethod
    def question_must_not_be_blank(cls,value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError('Question cannot be empty')
        return value

@app.get('/health')
def health_check():
    return {'status': 'ok'}

@app.get('/')
def Welcome_Page():
    return {'message': 'Welcome to MiniDoc AI'}

@app.post('/ask')
def ask_question(request: QuestionRequest):
    return {'received_question': request.question}


MAX_PDF_SIZE = 10 * 1024 *1024

@app.post('/upload-pdf')
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read(MAX_PDF_SIZE + 1)

    if len(contents) > MAX_PDF_SIZE:
        raise HTTPException(
            status_code=413,
            detail='PDF File is too large. Maximum size is 10 MB.'
        )
    if not contents.startswith(b'%PDF-'):
        raise HTTPException(
            status_code=400,
            detail='Invalid PDF File'
        )

    try:
        with fitz.open(stream=contents, filetype='pdf') as pdf:
            extracted_text = '\n'.join(
                page.get_text() for page in pdf
            )
            page_count=len(pdf)
    except(fitz.FileDataError, RuntimeError, ValueError):
        raise HTTPException(
            status_code=400,
            detail='Could not read the PDF File.'
        )

    return {
        'filename': file.filename,
        'page_count': page_count,
        'text': extracted_text
    }
    