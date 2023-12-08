import os
from pathlib import Path

from sqlalchemy import create_engine
from dotenv import load_dotenv

from app.modules.common.Database import Database
from app.modules.character.models import CharacterModel

PROJECT_DIR = Path(__file__).parent

load_dotenv()

engine = create_engine(os.environ['DB_URI'])
Base = Database

# don't run
# Database.metadata.create_all(engine, checkfirst=True)
# here, it will create tables here, and cause empty migrations in alembic
