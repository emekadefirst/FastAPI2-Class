from sqlmodel import SQLModel, create_engine, Field, Session

# Database configuration
db_url = "sqlite:///app.db"
engine = create_engine(db_url, echo=True)

# Create tables and database
def create_table_and_db():
    SQLModel.metadata.create_all(engine)


# Define Team model
class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquater: str


# Define Hero model
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str
    age: int
    team_id: int | None = Field(default=None, foreign_key="team.id")


# Ensure tables are created
create_table_and_db()


# Define a custom session class for adding data
class GetPostSession:
    def __init__(self, model, **kwargs):
        self.model = model
        self.kwargs = kwargs

    def add(self):
        with Session(engine) as session:
            data = self.model(**self.kwargs)
            session.add(data)
            session.commit()
            return f"Data has been saved: {data}"
        
    def get(self):
        with Session(engine) as session:
            data = session.query(self.model).all()
            return data

def get_user(Model, id):
    with Session(engine) as session:
        user = session.query(Model).filter(Model.id == id).first()
        return user


class RetrieveUpdateDelete:
    session = Session(engine)
    def __init__(self, model, id, **kwargs):
        self.model = model
        self.id = id
        self.data = kwargs

    def retrieve(self):
        return get_user(self.model, self.id) 

    def update(self, **kwargs):
        """Update a record with new data."""
        with Session(engine) as session:
            record = get_user(self.model, self.id)
            if record:
                for key, value in kwargs.items():
                    setattr(record, key, value)  # Update attributes
                session.add(record)
                session.commit()
                return f"Record updated: {record}"
            return f"No record found with ID {self.id}"

    def delete(self):
        with Session(engine) as session:
            data = session.query(self.model).filter(self.model.id == self.id).first()
            if data:
                session.delete(data)
                session.commit()
                return f"Data has been deleted: {data}"
            return f"No data found with id: {self.id}"
