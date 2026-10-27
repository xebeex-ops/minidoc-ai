from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Minidoc AI')

class QuestionRequest(BaseModel):
    question: str



@app.get('/health')
def health_check():
    return {'status': 'ok'}

@app.get('/')
def Welcome_Page():
    return {'message': 'Welcome to MiniDoc AI'}

@app.post('/ask')
def ask_question(request: QuestionRequest):
    return {'received_question': request.question}