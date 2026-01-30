#This folder contains operations to help us manage interactions between models and how the data is processed in the database.

def user_schema(user) -> dict:
    return {"id": str(user["_id"]),      #we have to make sure that id object is converted to string
            "username": user["username"],
            "email": user["email"]}


def users_schema(users) -> list:
    return [user_schema(user)for user in users]