from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI(title='Minidoc AI')

class QuestionRequest(BaseModel):
    question: str

    @field_validator('question')
    @classmethod
    def question_must_not_be_blank(cls,value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError('Question cannot be empy')
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