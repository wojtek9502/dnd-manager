import os

from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

from app.modules.user.services import UserTokenService

API_KEY_NAME = 'X-API-KEY'
API_KEY = os.environ['API_AUTH_MASTER_TOKEN']
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def _is_token_valid_with_main_token(api_key) -> bool:
    if api_key == API_KEY:
        return True
    return False


async def validate_api_key(api_key: str = Security(api_key_header)):
    user_token_service = UserTokenService()

    is_token_valid = user_token_service.is_token_valid(token=api_key)
    if not is_token_valid:
        is_token_valid = _is_token_valid_with_main_token(api_key=api_key)

    if not is_token_valid:
        raise HTTPException(status_code=401, detail='Invalid or missing API Key')
