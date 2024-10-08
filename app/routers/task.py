from fastapi import APIRouter
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

# from user import User

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks():
    pass


@router.get('/task_id')
async def task_by_id():
    pass


@router.get('/create')
async def create_task():
    pass


@router.get('/update')
async def update_task():
    pass


@router.get('/delete')
async def delete_task():
    pass


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates='tasks')


from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))
