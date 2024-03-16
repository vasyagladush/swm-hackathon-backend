from typing import Annotated
from fastapi import Body, APIRouter, Depends, HTTPException, Header
import jwt
from passlib.context import CryptContext

from auth.jwt_bearer import JWTBearer
from auth.jwt_handler import sign_jwt
from config.config import Settings
from database.user import add_user
from models.User import User
from schemas.user import UserData, UserSignIn

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

token_listener = JWTBearer()


@router.post("/login")
async def user_login(user_credentials: UserSignIn = Body(...)):
    user_exists = await User.find_one(User.username == user_credentials.username)
    if user_exists:
        password = hash_helper.verify(
            user_credentials.password, user_exists.password)
        if password:
            return sign_jwt(user_credentials.username)

        raise HTTPException(
            status_code=403, detail="Incorrect email or password")

    raise HTTPException(status_code=403, detail="Incorrect email or password")


@router.post("/", response_model=UserData)
async def user_signup(user: User = Body(...)):
    user_exists = await User.find_one(User.username == user.username)
    if user_exists:
        raise HTTPException(
            status_code=409, detail="User with email supplied already exists"
        )

    user.password = hash_helper.encrypt(user.password)
    new_user = await add_user(user)
    return new_user


@router.get("/", dependencies=[Depends(token_listener)], response_model=UserData)
async def get_user(Authorization: Annotated[str, Header()]):
    jwt_token = Authorization[6:].strip()
    username = jwt.decode(jwt_token, Settings(
    ).JWT_SECRET_KEY, algorithms=["HS256"])['user_id']

    user = await User.find_one(User.username == username)
    if not user:
        raise HTTPException(
            status_code=404, detail="No user found")
    return user