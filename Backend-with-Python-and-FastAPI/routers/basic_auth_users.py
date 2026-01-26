from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth_users", tags=["auth_users"], responses={404: {"message": "Not found"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "Irene": {
        "username": "Irene",
        "full_name": "Irene Martin",
        "email": "martincampoirene@gmail.com",
        "disabled": False,
        "password": "123456"        #real case, it should be encrypted
    },
    "Olga": {
        "username": "Olga",
        "full_name": "Olga Martin",
        "email": "martincampoolga@gmail.com",
        "disabled": True,
        "password": "122258"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid authentication credentials", 
            headers={"www-Authenticate": "Bearer"})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Inactive user")
    return user

    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    users_db = users_db.get(form.username)
    if not users_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The user is not correct")
    
    user = search_user_db(form.username)
    if form.password != user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The password is not correct")
    
    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/me")
async def me(user:User = Depends(current_user)):
    return user