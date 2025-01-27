import asyncio
from sqlmodel import Session
from sqlmodel.ext.asyncio.session import AsyncSession
from models import User, Message,  engine

from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///database.db"
maze = create_async_engine(DATABASE_URL, echo=False)


async def add_chat(message: str):
    session = AsyncSession(maze)
    message = Message(message=message)
    session.add(message)
    session.commit()
    return "Message saved"

def all_chat():
    session = Session(engine)
    chats = session.query(Message).all()
    return chats

# Create User
def create(username: str, email,  password: str):
    try:
        with Session(engine) as session:
            user = User(username=username, email=email, password=password)
            session.add(user)
            session.commit()
            return "User was sucessfully created"
    except Exception as e:
        return "User failed to create"


# Get all Users
def all_user():
    try:
        with Session(engine) as session:
            users = session.query(User).all()
            return users
    except Exception as e:
        return "Failed to get all users"


# Get User by ID
def user_by_id(id):
    try:
        with Session(engine) as session:
            user = session.query(User).filter(User.id == id).first()
            return user
    except Exception as e:
        return "Failed to get user by id"
