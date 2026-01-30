from typing import Optional
from fastapi import APIRouter, HTTPException, Query, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/userdb", tags=["userdb"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})


users_list = []

# Find all users
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

@router.get("/byquery", response_model=User)
async def user_by_query(
        id: Optional[str] = Query(None),
        username: Optional[str] = Query(None),
        email: Optional[str] = Query(None)):
    if not id and not username and not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide either 'id', 'name' or 'email'"
        )
    
    if id:
        return search_user("_id", ObjectId(id))
    if username:
        return search_user("username", username)
    if email:
        return search_user("email", email)

# Find user by id
@router.get("/{id}")
async def user(id: str): 
    return search_user("_id", ObjectId(id))

@router.post("/", response_model=User ,status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="The user already exist")
    else:
        user_dict = dict(user)
        del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    # Mongo uses _id; query by that, then map to schema
    new_user = user_schema(db_client.users.find_one({"_id": id}))      #Users will be created automatically as a folder in mongodb the first time you insert a user.
    return User(**new_user)                #local is the data base name

@router.put("/", response_model=User )
async def user(user: User):
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)

    except:
        return {"error": "The user has not been updated"}
    
    return search_user("_id", ObjectId(user.id))

@router.delete("/{id}")
async def user(id: str, status_code=status.HTTP_204_NO_CONTENT):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "User has not been eliminated"}

    
def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "Not user found"}
