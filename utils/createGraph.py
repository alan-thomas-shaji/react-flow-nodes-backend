from models.QueryModel import QueryModel
import networkx as nx

def checkIfDag(query: QueryModel):
    edges = []
    for edge in query.edges:
        edges.append((edge.source,edge.target))
    G = nx.DiGraph(edges)
    return len(list(nx.simple_cycles(G))) <= 0