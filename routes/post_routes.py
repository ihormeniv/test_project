from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import PostCreate, PostResponse
from app.services.post_service import create_post, get_posts, delete_post

router = APIRouter()


def extract_token(authorization: str) -> str:
    """Extract and validate the Bearer token from the Authorization header."""
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Invalid Authorization header")
    return authorization.split(" ")[1]


@router.post("/addpost", response_model=PostResponse)
def add_post(
    post: PostCreate,
    authorization: str = Header(...),
    db: Session = Depends(get_db)
):
    token = extract_token(authorization)
    return create_post(db, post, token)


@router.get("/getposts", response_model=list[PostResponse])
def get_user_posts(
    authorization: str = Header(...),
    db: Session = Depends(get_db)
):
    token = extract_token(authorization)
    return get_posts(db, token)


@router.delete("/deletepost")
def delete_user_post(
    post_id: int,
    authorization: str = Header(...),
    db: Session = Depends(get_db)
):
    token = extract_token(authorization)
    delete_post(db, post_id, token)
    return {"detail": "Post deleted"}