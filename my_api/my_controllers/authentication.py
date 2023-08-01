import logging
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response, encoders
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from my_modules import module_authentication
from my_modules.module_authentication import User, get_current_active_user
from self_logging import MyLogger

router = APIRouter()
my_logger = MyLogger(log_level=logging.INFO)
logger = my_logger.get_logger()


@router.post("/login", response_model=object)
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    print("form_data.username: ", form_data.username)
    user = await module_authentication.authenticate_user(form_data.username, form_data.password)
    print("user: ", user)
    if not user:
        logger.info(f"UNAUTHORIZED user with username {form_data.username}")
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
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=object)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
