from pydantic import BaseModel

class Edge(BaseModel):
    source: str
    sourceHandle: str
    target: str
    targetHandle: str