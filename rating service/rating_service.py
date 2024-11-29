from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Rating(BaseModel):
    book_id: int
    rating: int  # Rating out of 10

ratings = []

@app.post("/ratings/", response_model=Rating)
def create_rating(rating: Rating):
    ratings.append(rating)
    return rating

@app.get("/ratings/", response_model=List[Rating])
def read_ratings():
    return ratings

@app.get("/ratings/{book_id}", response_model=List[Rating])
def read_ratings_for_book(book_id: int):
    book_ratings = [r for r in ratings if r.book_id == book_id]
    if not book_ratings:
        raise HTTPException(status_code=404, detail="No ratings found for this book")
    return book_ratings
