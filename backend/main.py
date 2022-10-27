import uvicorn
from fastapi import FastAPI
from backend.services.scrape_service import ScrapeService

app = FastAPI(title="Quando joga o Benfica")

service = ScrapeService()


@app.get("/", tags=["Services"])
def home():
    return service.scrape_next_match_page()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
