from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from datetime import datetime
from .document_engine import generate_document

app = FastAPI(title="HRflow AI")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def handle_generate(
    document_type: str = Form(...),
    name: str = Form(...),
    position: str = Form(...),
    company: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form("N/A"),
    salary: str = Form("N/A"),
    notes: str = Form("")
):
    try:
        document_content = generate_document(
            doc_type=document_type,
            name=name,
            position=position,
            company=company,
            start_date=start_date,
            end_date=end_date,
            salary=salary,
            notes=notes
        )
        return JSONResponse(content={
            "success": True,
            "document": document_content,
            "date": datetime.now().strftime("%B %d, %Y")
        })
    except Exception as e:
        return JSONResponse(content={"success": False, "error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
