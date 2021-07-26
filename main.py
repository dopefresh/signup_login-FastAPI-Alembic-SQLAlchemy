from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

from token_password import authenticate_user, create_access_token, get_current_user
from schemas import Token, User
from logging import logger

from pydantic import BaseModel


app = FastAPI()


@app.post('/signup')
async def signup(form_data: OAuth2PasswordRequestForm = Depends()):
    try: 
        user = token_password.create_user(form_data.username, form_data.password)
        return RedirectResponse('/login', status_code=302)
    except Exception as e:
        logger.error(e)


@app.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user






