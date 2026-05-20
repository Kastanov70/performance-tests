from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from pydantic import BaseModel, EmailStr, RootModel

app = FastAPI()

users_router = APIRouter(
    prefix="/api/v1/users",
    tags=["users-service"],
)

class UserIn(BaseModel):
    username: str
    email: EmailStr

class UserOut(UserIn):
    id: int

class UserStore(RootModel):
    root: list[UserOut]

    def find(self, user_id: int) -> UserOut | None:
        return next(filter(lambda user: user.id == user_id, self.root), None)

    def create(self, user_in: UserIn) -> UserOut:
        user = UserOut(id=len(self.root) + 1, **user_in.model_dump())
        self.root.append(user)
        return user

    def update_user(self, user_id: int, user_in: UserIn) -> UserOut:
        index = next(index for index, user in enumerate(self.root) if user.id == user_id)
        updated = UserOut(id=user_id, **user_in.model_dump())
        self.root[index] = updated
        return updated

    def delete(self, user_id: int) -> None:
        self.root =  [user for user in self.root if user.id != user_id]

store = UserStore(root=[])

@users_router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    if not(user := store.find(user_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID: {user_id} not found"
        )
    else:
        return user

@users_router.post("", response_model=UserOut)
async def create_user(user: UserIn):
    return  store.create(user)

@users_router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    if not store.find(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID: {user_id} not found"
        )
    else:
        return store.update_user(user_id, user)

@users_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    if not store.find(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID: {user_id} not found"
        )
    else:
        store.delete(user_id)

@users_router.get("", response_model=UserStore)
async def get_users():
    return store.root

app.include_router(users_router)