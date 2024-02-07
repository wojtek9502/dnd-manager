import os
import logging
import sys
import traceback
from pathlib import Path

from sqlalchemy import create_engine
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.responses import RedirectResponse

# db
from app.modules.common.Database import Database
from app.modules.character.models import CharacterModel
from app.modules.user.models import UserModel

PROJECT_DIR = Path(__file__).parent
LOGS_DIR = Path(PROJECT_DIR, 'logs')
logger = logging.getLogger()

load_dotenv()

engine = create_engine(os.environ['DB_URI'])
Base = Database

# don't run
# Database.metadata.create_all(engine, checkfirst=True)
# here, it will create tables here, and cause empty migrations in alembic


def handle_exceptions(*exc_info):
    msg = "".join(traceback.format_exception(*exc_info))
    logger.error(f"An unhandled exception: {msg}")


sys.excepthook = handle_exceptions

app = FastAPI(
    docs_url=f'/swagger-ui',
    redoc_url=f'/redoc',
    openapi_url=f'/openapi.json',
    dependencies=[],
)

@app.get("/", include_in_schema=False)
async def redirect_to_swagger():
    return RedirectResponse(url='/swagger-ui')


from app.modules.api.user.router import router as user_router
from app.modules.api.tools.router import router as tools_router

app.include_router(user_router)
app.include_router(tools_router)
