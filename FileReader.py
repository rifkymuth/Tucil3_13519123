import matplotlib.pyplot as plt
import networkx as nx
import csv
import json


def read_config():
    f = open('config.json', 'r')
    data = json.load(f)
    f.close()
    return data['path']


def create_graph(G):
    path = read_config()
    f = open(path, 'r')
    input_text = f.read().split("---")
    input_line_nodes = input_text[0].strip().split('\n')
    input_nodes = []
    x_dplc = 0
    y_dplc = 0
    for l in input_line_nodes:
        input_nodes.append(l.split(','))
        firstNode = False
    for l in input_nodes:
        if (not firstNode):
            x_dplc = float(l[2])
            y_dplc = float(l[1])
            firstNode = True
        name = l[0].strip()
        posX = (float(l[2]) - x_dplc) * 100000
        posY = (float(l[1]) - y_dplc) * 100000
        pos = (posX, posY)
        G.add_node(name, pos=pos)
    input_line_edges = input_text[1].strip().split('\n')
    input_edges = []
    for edge in input_line_edges:
        e = edge.split(',')
        input_edges.append((e[0].strip(), e[1].strip()))
    G.add_edges_from(input_edges)
    nx.set_edge_attributes(G, 'k', 'color')
    f.close()
