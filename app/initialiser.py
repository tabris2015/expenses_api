from sqlmodel import SQLModel
from app.database.session import engine
from app.models.product import Product


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()


if __name__ == '__main__':
    main()
