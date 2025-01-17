from sqlmodel import SQLModel, create_engine, Field


db_name = "datahb.db"
url_param = f"sqlite:///{db_name}"
engine = create_engine(url_param, echo=True)


def create_db_and_table():
    return SQLModel.metadata.create_all(engine)


class User(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    username : str = Field(max_length=50, unique=True)
    email : str = Field(max_length=100, unique=True)
    password : str | None


create_db_and_table()
