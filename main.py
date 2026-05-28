import uvicorn
import os

if __name__ == "__main__":
    # Ensure port 8003 is used to avoid conflicts with common ports
    uvicorn.run("app.main:app", host="127.0.0.1", port=8003, reload=True)
