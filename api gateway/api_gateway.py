from fastapi import FastAPI, Request
import httpx

app = FastAPI()

BOOK_SERVICE_URL = "http://book_service:8000"
RATING_SERVICE_URL = "http://rating_service:8001"

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(full_path: str, request: Request):
    service_url = BOOK_SERVICE_URL if "books" in full_path else RATING_SERVICE_URL
    url = f"{service_url}/{full_path}"
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers=request.headers.raw,
            content=await request.body()
        )
    return response
