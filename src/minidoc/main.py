from fastapi import FastAPI

app = FastAPI(title='Minidoc AI')

@app.get('/health')
def health_check():
    return {'status': 'ok'}