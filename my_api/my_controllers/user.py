from fastapi import APIRouter, HTTPException

router = APIRouter()

# @router.post()
#
# # Dummy data to simulate users (replace this with your database interaction)
# users = [
#     {"id": 1, "name": "John Doe"},
#     {"id": 2, "name": "Jane Smith"},
# ]
#
# @router.get("/users/{user_id}", response_model=dict)
# def get_user(user_id: int):
#     user = next((user for user in users if user["id"] == user_id), None)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
#
# @router.post("/users/", response_model=dict)
# def create_user(name: str):
#     new_user = {"id": len(users) + 1, "name": name}
#     users.append(new_user)
#     return new_user
