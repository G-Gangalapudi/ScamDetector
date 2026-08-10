from pydantic import BaseModel

class EventBase(BaseModel):
    name: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
