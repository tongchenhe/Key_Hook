from sqlalchemy import Column, Integer, Identity
from sqlalchemy.orm import relationship
from orm_base import Base

from HookDoorOpening import HookDoorOpening

class Hook(Base):
    __tablename__ = 'hooks'
    hook_number = Column('hook_number', Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)

    doors_list = relationship("HookDoorOpening", back_populates="hook")
    keys_list = relationship("Key", back_populates="hook")

    def __init__(self):
        # self.hook_number = hook_number

        self.keys_list = []
        self.doors_list = []

    def open_door(self, door):
        if door in self.doors_list:
            return
        
        onOpen = HookDoorOpening(self, door)
        self.doors_list.append(onOpen)
        door.hooks_list.append(onOpen)