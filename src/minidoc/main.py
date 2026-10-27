from fastapi import FastAPI

app = FastAPI(title='Minidoc AI')

@app.get('/health')
def health_check():
    return {'status': 'ok'}

@app.get('/')
def Welcome_Page():
    return {'message': 'Welcome to MiniDoc AI'}