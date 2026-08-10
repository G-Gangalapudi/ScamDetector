from pydantic import BaseModel

class AnalysisBase(BaseModel):
    summary: str

class AnalysisCreate(AnalysisBase):
    pass

class Analysis(AnalysisBase):
    id: int
