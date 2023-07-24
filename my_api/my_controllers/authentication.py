from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from . import module_authentication
from .module_authentication import fake_users_db

# from .module_authentication import *
# from module_authentication import  Token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

router = APIRouter()


@router.post("/login", response_model=dict)
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    # Depends() can be problem perphaps not empty auto2
    user = module_authentication.authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=module_authentication.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = module_authentication.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    # response.set_cookie(
    #     key="Authorization", value=f"Bearer {encoders.jsonable_encoder(access_token)}",
    #     httponly=True
    # )
    # it is not setting the cookie (maybe)
    return {"access_token": access_token, "token_type": "bearer"}
