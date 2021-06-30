import io
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/image")
def image_endpoint():
    return FileResponse("./out.png")
