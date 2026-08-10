from pydantic import BaseModel

class IndicatorBase(BaseModel):
    value: str

class IndicatorCreate(IndicatorBase):
    pass

class Indicator(IndicatorBase):
    id: int
