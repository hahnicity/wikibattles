import csv
import re

import networkx as nx


def parse(filename):
    reader = csv.reader(open(filename, 'r'), delimiter=',')
    data = [row for row in reader]
    return parse_directed(data)


def parse_directed(data):
    digraph = nx.DiGraph()

    for row in data:
        node_a = format_key(row[0])
        node_b = format_key(row[2])
        val_a = digits(row[1])
        val_b = digits(row[3])

        if val_a >= val_b:
            # Weighted toward a so directed edge from b to a
            digraph.add_edge(node_b, node_a)
        else:
            # Weighted toward b so directed edge from a to b
            digraph.add_edge(node_a, node_b)

    return digraph


def digits(val):
    return int(re.sub("\D", "", val))


def format_key(key):
    key = key.strip()
    if key.startswith('"') and key.endswith('"'):
        key = key[1:-1]
    return key
