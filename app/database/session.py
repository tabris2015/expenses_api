from sqlmodel import Session, create_engine
from app.core import settings

engine = create_engine(settings.DATABASE_URI)


def get_session():
    with Session(engine) as session:
        yield session
