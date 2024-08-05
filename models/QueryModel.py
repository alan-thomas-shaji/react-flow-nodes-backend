from typing import List
from pydantic import BaseModel
from models.Edge import Edge
from models.Node import Node

class QueryModel(BaseModel):
    nodes: List[Node]
    edges: List[Edge]