from pydantic import BaseModel

class Node(BaseModel):
    id: str
    type: str