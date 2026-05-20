import uvicorn
from fastapi import FastAPI, Query, Path, Body, APIRouter, HTTPException, Depends
from pydantic import BaseModel
from starlette import status


class User(BaseModel):
    username: str
    email: str
    age: int

class UserResponse(BaseModel):
    username: str
    email: str
    message: str

def validate_min_age(min_age: int=18):
    def checker(user:User):
        if user.age < min_age:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Age must be greater than or equal to {min_age}",
            )
        return user
    return checker

app = FastAPI(title="FastAPI Basics")

router = APIRouter(
    prefix="/api/v1",
    tags=["FastAPI Basics"],
)


@router.get("/basics/{item_id}")
async def get_basics(
        name: str = Query(
            default="Alice",
            description="The name of the person to look up",
        ),
        item_id: int = Path(
            description="The ID of the item to look up", )
):
    return {
        "message": f"Hello {name}",
        "description": f"Item number {item_id}",
    }

@router.post("/basics/users", response_model=UserResponse)
async def create_user(user: User=Body(description="New user data")):
    return UserResponse(
        username=user.username,
        email=user.email,
        message="User created successfully"
    )

@router.post("/basics/register", summary="Register a new user")
async def register_user(user: User= Depends(validate_min_age(21))):
    return {
        "email": user.email,
        "age": user.age,
        "message": f"User {user.username} created successfully"
    }

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "fastapi_basics:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
