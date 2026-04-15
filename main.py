from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return JSONResponse(
        content={"message": "API is running"}, status_code=status.HTTP_200_OK
    )


@app.get("/health")
async def health():
    return JSONResponse(content={"message": "healthy"}, status_code=status.HTTP_200_OK)


@app.get("/me")
async def me():
    return JSONResponse(
        content={
            "name": "Nehemiah Adoba Daniel",
            "email": "danielnehemiah15@gmail.com",
            "github": "https://github.com/nehecodes",
        },
        status_code=status.HTTP_200_OK,
    )
