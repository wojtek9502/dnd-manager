import logging
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.modules.api import auth
from app.modules.api.user.schema import LoginResponseSchema, UserResponseSchema, UserUuidResponseSchema, LoginRequestSchema, \
    UserCreateRequestSchema, UserUpdateRequestSchema
from app.modules.common.BaseRepository import NotFoundEntityError
from app.modules.user.exceptions import UserLoginPasswordInvalidError
from app.modules.user.repositories import UserRepository
from app.modules.user.services import UserService, UserTokenService

router = APIRouter(prefix='/user')
logger = logging.getLogger()


@router.post("/login", response_model=LoginResponseSchema)
async def login(request: LoginRequestSchema):
    user_service = UserService()
    user_token_service = UserTokenService()

    try:
        user_logged_jwt_token = user_service.login_user(
            username=request.username,
            password_clear=request.password
        )
    except (NotFoundEntityError, UserLoginPasswordInvalidError):
        msg = "Invalid username or password"
        raise HTTPException(status_code=401, detail=msg)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    user_entity = user_service.find_by_username(username=request.username)
    if not user_entity:
        raise HTTPException(status_code=404, detail=f"Not found user {request.username}")

    entity = user_token_service.create_token(
        token=user_logged_jwt_token,
        user_id=user_entity.id
    )

    return LoginResponseSchema(
        token=entity.token
    )


@router.get("/", response_model=List[UserResponseSchema],
            dependencies=[Depends(auth.validate_api_key)])
async def find_all():
    service = UserService()

    try:
        entities = service.find_all()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

    users_response: List[UserResponseSchema] = []
    for entity in entities:
        entity_data = UserResponseSchema(
            id=entity.id,
            username=entity.username,
        )
        users_response.append(entity_data)
    return users_response


@router.get("/by_username", response_model=UserResponseSchema,
            dependencies=[Depends(auth.validate_api_key)])
async def find_by_username(username: str):
    repo = UserRepository()

    try:
        entity = repo.find_by_username(
            username=username,
        )
    except Exception:
        raise HTTPException(status_code=404, detail=f"Not found user with username: '{username}'")

    return UserResponseSchema(
        id=entity.id,
        username=entity.username
    )


@router.post("/create", response_model=UserResponseSchema,
             dependencies=[Depends(auth.validate_api_key)])
async def create(request: UserCreateRequestSchema):
    service = UserService()

    try:
        entity = service.create_user(
            username=request.username,
            password_clear=request.password
        )
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail="User create error")

    return UserResponseSchema(
        id=entity.id,
        username=entity.username
    )


@router.post("/update", response_model=UserResponseSchema,
             dependencies=[Depends(auth.validate_api_key)])
async def update(request: UserUpdateRequestSchema):
    service = UserService()
    try:
        entity = service.update_user(
            user_id=request.user_id,
            password_clear=request.password
        )
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail="User update error")

    return UserResponseSchema(
        id=entity.id,
        username=entity.username
    )


@router.delete("/delete", response_model=UserUuidResponseSchema,
               dependencies=[Depends(auth.validate_api_key)])
async def delete(user_id: UUID):
    service = UserService()
    try:
        entity_id = service.delete_user(
            user_id=user_id,
        )
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail="User delete error")

    return UserUuidResponseSchema(id=entity_id)
