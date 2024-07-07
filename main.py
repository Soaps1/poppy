from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sum import add_numbers

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/count", response_class=HTMLResponse)
async def count_characters(request: Request, sentence: str = Form(...)):
    char_count = len(sentence)
    return templates.TemplateResponse("index.html", {"request": request, "char_result": char_count})

@app.post("/sum", response_class=HTMLResponse)
async def sum_numbers(request: Request, num1: int = Form(...), num2: int = Form(...)):
    result = add_numbers(num1, num2)
    return templates.TemplateResponse("index.html", {"request": request, "sum_result": result})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
