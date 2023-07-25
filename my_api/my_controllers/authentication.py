from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response, encoders
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from my_modules import module_authentication
from my_modules.module_authentication import User, get_current_active_user

# from .module_authentication import *
# from module_authentication import  Token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

router = APIRouter()


@router.post("/login", response_model=dict)
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    # Depends() can be problem perphaps not empty auto2
    print(form_data.username)
    user = await module_authentication.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=module_authentication.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = module_authentication.create_access_token(
        data={"sub": user['user_name']}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="Authorization", value=f"Bearer {encoders.jsonable_encoder(access_token)}",
        httponly=True
    )
    # it is not setting the cookie (maybe)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user