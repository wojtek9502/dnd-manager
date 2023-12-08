from pathlib import Path

from sqlalchemy import create_engine

from app.modules.common.Database import Database

from app.modules.character.models import CharacterModel

PROJECT_DIR = Path(__file__).parent

engine = create_engine(f"sqlite:///{PROJECT_DIR}/db.sql")
Database.metadata.create_all(engine, checkfirst=True)