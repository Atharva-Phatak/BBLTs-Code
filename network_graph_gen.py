import json 
import pandas as pd 
import os 
import networkx as nx
from copy import deepcopy


def readNestedJson(path,levels):
    nestedData = {}
    for level in range(1, levels):
            dataPath = f"{path}level-{level}/data.json"
            data = json.load(open(dataPath))
            nesteData.update(data)
    return nestedData

def convertToGraph(data):
    graph = nx.DiGraph()
    for author, coAuthors in data:
        #if len(self.authors[k]) > no_edges:
        for coauthor in coAuthors:
            graph.add_edge(author,coauthor)
    

def saveJson(fname, data):
    with open(fname, "w") as f:
        json.dumps(data, f, indent = 4)

def findCollaborations(citationData, fname):
    authors = {}
    for title, values in citationData.items(): 
        if values != [[]]: #[paper, [ravi, vijay, x]] 
            for paperTitle, paperAuthors in values:  
                if paperAuthors:
                    for author in paperAuthors: 
                        x = deepcopy(paperAuthors)
                        if len(x) > 1:
                            x.remove(author)
                            if author in authors:
                                authors[author]  += x
                            else:
                                authors[author] = x
    for author, coAuthors in authors.items():
        authors[author] = list(set(coAuthors))
    return authors
    #convertToGraph(data = authors)
    #saveJson(fname, )

if __name__ == "__main__":
    levels = 1
    year = 2015
    path = f"../related_data/ppsh/Temporal-Analysis/JSON/year-{year}/"
    citationData = readNestedJson(path, levels)
    authors = findCollaborations(citationData, f"year-{year}-colabs.json")

    


