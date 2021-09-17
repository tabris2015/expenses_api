from sqlmodel import SQLModel
from app.database.session import engine
from app.models.product import Product
from app.models.expense import Expense
from app.models.category import Category


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    print("Creating Database tables...")
    create_db_and_tables()


if __name__ == '__main__':
    main()
