from fastapi import FastAPI
from models.QueryModel import QueryModel
from utils.createGraph import checkIfDag
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def parse_pipeline(queryModel: QueryModel):
    is_dag = checkIfDag(queryModel)
    return {"num_nodes": len(queryModel.nodes), "num_edges": len(queryModel.edges), "is_dag": is_dag}
