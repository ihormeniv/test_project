from fastapi import FastAPI
from app.routes import user_routes, post_routes
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(user_routes.router, prefix="/user", tags=["User"])
app.include_router(post_routes.router, prefix="/post", tags=["Post"])
